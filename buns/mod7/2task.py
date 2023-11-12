def memoize(func):
    cache = {}
    original_name = func.__name__
    original_doc = func.__doc__
 
    def wrapper(*args):
        if args not in cache:
            result = func(*args)
            cache[args] = result
        return cache[args]
 
    wrapper.__name__ = original_name
    wrapper.__doc__ = original_doc
 
    return wrapper
 
@memoize
def fibonacci_recursive(n):
    if n <= 2:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
 
@memoize
def fibonacci_memoized(n):
    if n <= 2:
        return 1
    return fibonacci_memoized(n-1) + fibonacci_memoized(n-2)
 
# провеепрка
for i in range(1, 11):
    result_recursive = fibonacci_recursive(i)
    result_memoized = fibonacci_memoized(i)
    print(f"fibonacci_recursive({i}) = {result_recursive}")
    print(f"fibonacci_memoized({i}) = {result_memoized}")
    print("-" * 30)
    
