def logging_decorator(function):
    #Function describe name of funcions and returned result
    def wrapper(*args):
        print( f"You called {function.__name__}{(args)}")
        result = function(args[0], args[1], args[2])
        print(f"It returned: {result}")
    return wrapper

@logging_decorator
def a_funnction(a, b, c):
    return a * b * c

a_funnction(1,2,3)