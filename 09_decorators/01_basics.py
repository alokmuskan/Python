from functools import wraps

def my_decorator(func):

    @wraps
    def wrapper(func):
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello from decorators class from chai code")

greet()

print(greet.__name__)