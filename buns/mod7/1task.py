def validate_args(func):
    def wrapper(*args):
        if len(args) != 1:
            return "нету аргументов" if len(args) < 1 else "слишком много аргументов"
 
        arg = args[0]
 
        if not isinstance(arg, int):
            return "неверный тип"
 
        if arg < 0:
            return "отрицательный аргумент"
 
        return func(*args)
 
    return wrapper
 
 
@validate_args
def example_function(x):
    return f"аргумент - {x}"
print(example_function(5))          
print(example_function("invalid"))  
print(example_function(-3))         
print(example_function(1, 2))        
print(example_function())            