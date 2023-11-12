import time
 
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"скорость выполнения функции {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper
 
def memoize(func):
    cache = {}
 
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
 
    return wrapper
 
@timer
def fibonacci_recursive(n):
    if n <= 2:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
 
@timer
@memoize
def fibonacci_memoized(n):
    if n <= 2:
        return 1
    return fibonacci_memoized(n-1) + fibonacci_memoized(n-2)
 
print(fibonacci_recursive(30))
print(fibonacci_memoized(30))