

def dec_do_twice(count):
    def do_twice(fn):
        def wrapper_do_twice(*args,**kwargs):
            for _ in range(count):
                fn(*args,**args)
                fn(*args,**args)
        return wrapper_do_twice
    return do_twice

@dec_do_twice(count=2)
def hello():
    print("hello")

@dec_do_twice(count=2)
def greet(name):
    print("hello" + name)





