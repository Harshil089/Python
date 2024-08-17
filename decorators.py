# def new_decorator(original_func):
#     def wrap_function():
#         print("some code")
#         original_func()
#         print("some other code")
#     return wrap_function()
# @new_decorator
# def func_needs_decorator():
#     print("I want to be decorated")
# func_needs_decorator()

def my_decorator (func) :
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
say_hello()
