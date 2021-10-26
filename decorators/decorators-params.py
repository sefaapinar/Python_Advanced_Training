


def do_twice(func):
    def wrapper_do_twice(*args,**kwargs):
        func(*args,**kwargs)
        func(*args,**kwargs)
    return wrapper_do_twice

@do_twice
def hello():
    print("Hello")

@do_twice
def greet(msg):
    print("hi" + msg)

@do_twice
def return_greeting(name):
    print("greeting function")
    return f"hello,{name}"


greet("World")

return_greeting("Sefa")
print(return_greeting("Sefa"))
# hello()