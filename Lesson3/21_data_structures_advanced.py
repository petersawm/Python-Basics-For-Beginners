# Async Programming - Concurrent code execution

import asyncio
import time

# SYNCHRONOUS vs ASYNCHRONOUS

# Synchronous (blocking)
def sync_task(name, delay):
    print(f"{name} starting...")
    time.sleep(delay)
    print(f"{name} completed!")

def run_sync():
    start = time.time()
    sync_task("Task 1", 2)
    sync_task("Task 2", 2)
    sync_task("Task 3", 2)
    print(f"Total time: {time.time() - start:.2f}s")

# Takes 6 seconds total
# run_sync()


# Asynchronous (non-blocking)
async def async_task(name, delay):
    print(f"{name} starting...")
    await asyncio.sleep(delay)
    print(f"{name} completed!")

async def run_async():
    start = time.time()
    await asyncio.gather(
        async_task("Task 1", 2),
        async_task("Task 2", 2),
        async_task("Task 3", 2)
    )
    print(f"Total time: {time.time() - start:.2f}s")

# Takes only 2 seconds (runs concurrently)
# asyncio.run(run_async())


# BASIC ASYNC/AWAIT SYNTAX

# Async function definition
async def simple_async():
    print("Starting async function")
    await asyncio.sleep(1)
    print("Async function completed")
    return "Result"

# Running async function
# result = asyncio.run(simple_async())
# print(result)


# MULTIPLE ASYNC TASKS

async def fetch_data(source, delay):
    print(f"Fetching from {source}...")
    await asyncio.sleep(delay)
    return f"Data from {source}"

async def main():
    # Run tasks concurrently
    results = await asyncio.gather(
        fetch_data("API 1", 2),
        fetch_data("API 2", 1),
        fetch_data("API 3", 3)
    )
    
    for result in results:
        print(result)

# asyncio.run(main())


# ASYNC WITH ERROR HANDLING

async def risky_task(task_id):
    try:
        print(f"Task {task_id} starting")
        await asyncio.sleep(1)
        
        if task_id == 2:
            raise ValueError(f"Task {task_id} failed")
        
        print(f"Task {task_id} completed")
        return f"Result {task_id}"
    except ValueError as e:
        print(f"Error: {e}")
        return None

async def run_risky_tasks():
    results = await asyncio.gather(
        risky_task(1),
        risky_task(2),
        risky_task(3),
        return_exceptions=True  # Don't stop on error
    )
    
    for i, result in enumerate(results, 1):
        print(f"Task {i} result: {result}")

# asyncio.run(run_risky_tasks())


# TIMEOUTS

async def slow_operation():
    print("Starting slow operation...")
    await asyncio.sleep(5)
    return "Done"

async def with_timeout():
    try:
        result = await asyncio.wait_for(
            slow_operation(),
            timeout=2.0  # 2 second timeout
        )
        print(result)
    except asyncio.TimeoutError:
        print("Operation timed out!")

# asyncio.run(with_timeout())


# ASYNC GENERATORS

async def async_number_generator(n):
    for i in range(n):
        await asyncio.sleep(0.5)
        yield i

async def consume_async_gen():
    async for num in async_number_generator(5):
        print(f"Got number: {num}")

# asyncio.run(consume_async_gen())


# PRACTICAL: Web scraping with asyncio
# Note: Requires aiohttp library: pip install aiohttp

"""
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

urls = [
    'http://example.com',
    'http://example.org',
    'http://example.net'
]

# results = asyncio.run(fetch_multiple_urls(urls))
"""


# ASYNC CONTEXT MANAGERS

class AsyncDatabase:
    async def __aenter__(self):
        print("Opening database connection")
        await asyncio.sleep(0.5)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection")
        await asyncio.sleep(0.5)
    
    async def query(self, sql):
        print(f"Executing: {sql}")
        await asyncio.sleep(1)
        return "Query result"

async def use_database():
    async with AsyncDatabase() as db:
        result = await db.query("SELECT * FROM users")
        print(result)

# asyncio.run(use_database())


# TASKS vs GATHER

async def task_example(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")
    return f"{name} result"

async def using_tasks():
    # Create tasks
    task1 = asyncio.create_task(task_example("Task 1", 2))
    task2 = asyncio.create_task(task_example("Task 2", 1))
    
    # Do other work while tasks run
    print("Doing other work...")
    
    # Wait for tasks
    result1 = await task1
    result2 = await task2
    
    print(f"Results: {result1}, {result2}")

# asyncio.run(using_tasks())


# RATE LIMITING ASYNC REQUESTS

import asyncio
from asyncio import Semaphore

async def rate_limited_request(semaphore, request_id):
    async with semaphore:  # Only allows N concurrent requests
        print(f"Request {request_id} starting")
        await asyncio.sleep(1)
        print(f"Request {request_id} completed")
        return f"Result {request_id}"

async def run_rate_limited():
    semaphore = Semaphore(3)  # Max 3 concurrent requests
    
    tasks = [
        rate_limited_request(semaphore, i)
        for i in range(10)
    ]
    
    results = await asyncio.gather(*tasks)
    return results

# asyncio.run(run_rate_limited())


# ASYNC QUEUE

async def producer(queue, producer_id):
    for i in range(5):
        item = f"Item {i} from Producer {producer_id}"
        await queue.put(item)
        print(f"Produced: {item}")
        await asyncio.sleep(0.5)

async def consumer(queue, consumer_id):
    while True:
        item = await queue.get()
        print(f"Consumer {consumer_id} consumed: {item}")
        await asyncio.sleep(1)
        queue.task_done()

async def producer_consumer_example():
    queue = asyncio.Queue()
    
    # Start producers
    producers = [
        asyncio.create_task(producer(queue, i))
        for i in range(2)
    ]
    
    # Start consumers
    consumers = [
        asyncio.create_task(consumer(queue, i))
        for i in range(3)
    ]
    
    # Wait for producers to finish
    await asyncio.gather(*producers)
    
    # Wait for queue to be empty
    await queue.join()
    
    # Cancel consumers
    for c in consumers:
        c.cancel()

# asyncio.run(producer_consumer_example())


# PRACTICAL: Async file operations
# Note: Requires aiofiles library: pip install aiofiles

"""
import aiofiles

async def read_file_async(filename):
    async with aiofiles.open(filename, 'r') as file:
        co