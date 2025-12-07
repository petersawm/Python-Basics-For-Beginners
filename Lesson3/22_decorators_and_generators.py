# Decorators and Generators - Advanced Python concepts

# DECORATORS - Functions that modify other functions

# Basic decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call

# Without @ syntax (same result)
def say_goodbye():
    print("Goodbye!")

say_goodbye = my_decorator(say_goodbye)
say_goodbye()


# Decorator with arguments
def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@decorator_with_args
def add(a, b):
    return a + b

add(5, 3)


# Timing decorator
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return "Done"

slow_function()


# Logging decorator
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def multiply(x, y):
    return x * y

multiply(4, 5)


# Authentication decorator
def require_auth(func):
    def wrapper(user, *args, **kwargs):
        if not user.get('authenticated'):
            print("Access denied!")
            return None
        return func(user, *args, **kwargs)
    return wrapper

@require_auth
def view_profile(user):
    print(f"Welcome {user['name']}")

user1 = {'name': 'Peter', 'authenticated': True}
user2 = {'name': 'Guest', 'authenticated': False}

view_profile(user1)  # Works
view_profile(user2)  # Denied


# Cache decorator (memoization)
def cache_decorator(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print(f"Using cached result for {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@cache_decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))
print(fibonacci(5))  # Uses cache


# Multiple decorators
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclamation_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!!!"
    return wrapper

@exclamation_decorator
@uppercase_decorator
def greet(name):
    return f"hello {name}"

print(greet("Peter"))  # HELLO PETER!!!


# Decorator with parameters
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hi():
    print("Hi!")

say_hi()  # Prints "Hi!" three times


# Class-based decorator
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def process_data():
    print("Processing...")

process_data()
process_data()
process_data()


# GENERATORS - Lazy iterators

# Basic generator
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)

# Generator vs List
# List - all in memory at once
def get_numbers_list(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# Generator - one at a time (memory efficient)
def get_numbers_generator(n):
    for i in range(n):
        yield i ** 2

# Memory difference is huge for large n
import sys
nums_list = get_numbers_list(1000)
nums_gen = get_numbers_generator(1000)

print(f"List size: {sys.getsizeof(nums_list)} bytes")
print(f"Generator size: {sys.getsizeof(nums_gen)} bytes")


# Generator expression (like list comprehension)
# List comprehension
squares_list = [x**2 for x in range(10)]

# Generator expression
squares_gen = (x**2 for x in range(10))

print(sum(squares_gen))  # Uses generator


# Fibonacci generator
def fibonacci_gen(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for num in fibonacci_gen(10):
    print(num, end=" ")
print()


# File reading generator (memory efficient)
def read_large_file(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            yield line.strip()

# Usage:
# for line in read_large_file('huge_file.txt'):
#     process(line)


# Generator with send()
def echo_generator():
    while True:
        received = yield
        if received is not None:
            print(f"Received: {received}")

gen = echo_generator()
next(gen)  # Prime the generator
gen.send("Hello")
gen.send("World")


# Practical example: Data pipeline
def read_data():
    """Simulate reading data"""
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for item in data:
        yield item

def filter_even(numbers):
    """Filter even numbers"""
    for num in numbers:
        if num % 2 == 0:
            yield num

def square_numbers(numbers):
    """Square each number"""
    for num in numbers:
        yield num ** 2

# Chain generators
pipeline = square_numbers(filter_even(read_data()))
result = list(pipeline)
print(f"Pipeline result: {result}")


# Infinite generator
def infinite_counter(start=0):
    count = start
    while True:
        yield count
        count += 1

# Usage with islice
from itertools import islice
counter = infinite_counter()
first_10 = list(islice(counter, 10))
print(first_10)


# Generator for batching
def batch_generator(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

data = list(range(20))
for batch in batch_generator(data, 5):
    print(f"Batch: {batch}")


# Practical: CSV row generator
def csv_reader(filename):
    """Read CSV file line by line"""
    with open(filename, 'r') as file:
        headers = next(file).strip().split(',')
        for line in file:
            values = line.strip().split(',')
            yield dict(zip(headers, values))

# Usage:
# for row in csv_reader('data.csv'):
#     process_row(row)


# Performance comparison
import time

def performance_test():
    # Using list
    start = time.time()
    numbers_list = [x**2 for x in range(1000000)]
    result = sum(numbers_list)
    list_time = time.time() - start
    
    # Using generator
    start = time.time()
    numbers_gen = (x**2 for x in range(1000000))
    result = sum(numbers_gen)
    gen_time = time.time() - start
    
    print(f"List time: {list_time:.4f}s")
    print(f"Generator time: {gen_time:.4f}s")

performance_test()


# Combining decorators and generators
def uppercase_generator(gen_func):
    def wrapper(*args, **kwargs):
        for item in gen_func(*args, **kwargs):
            yield item.upper()
    return wrapper

@uppercase_generator
def word_generator():
    words = ['hello', 'world', 'python']
    for word in words:
        yield word

for word in word_generator():
    print(word)


# Real-world example: Rate limiter decorator
import time

def rate_limit(calls_per_second):
    min_interval = 1.0 / calls_per_second
    last_called = [0.0]
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            left_to_wait = min_interval - elapsed
            if left_to_wait > 0:
                time.sleep(left_to_wait)
            
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
        return wrapper
    return decorator

@rate_limit(calls_per_second=2)
def api_call():
    print("Making API call...")
    return "Response"

# Only allows 2 calls per second
for i in range(5):
    print(f"Call {i+1}")
    api_call()


# Generator for streaming data
def stream_processor(stream):
    """Process streaming data"""
    buffer = []
    for item in stream:
        buffer.append(item)
        if len(buffer) >= 5:  # Process in chunks
            yield sum(buffer)
            buffer = []
    
    # Process remaining items
    if buffer:
        yield sum(buffer)

data_stream = range(23)
for chunk_sum in stream_processor(data_stream):
    print(f"Chunk sum: {chunk_sum}")


# Decorator best practices
from functools import wraps

def better_decorator(func):
    @wraps(func)  # Preserves function metadata
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

@better_decorator
def my_function():
    """Original docstring"""
    pass

print(my_function.__name__)  # Prints 'my_function' not 'wrapper'
print(my_function.__doc__)   # Prints original docstring