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
def fibonacci(n):
    """
    рпекурсивная функция для вычисления числа фибоначчи.
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
 
print(fibonacci.__name__)  
print(fibonacci.__doc__) 