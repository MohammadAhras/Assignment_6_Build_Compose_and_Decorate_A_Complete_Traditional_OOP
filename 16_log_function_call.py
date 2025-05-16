def log_function_call(func):
    def wrapper(*arg, **kwargs):
        print("Function is being called")
        return func(*arg, **kwargs)
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()