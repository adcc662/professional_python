def decorator(fun):
    def wrapper():
        print('This is added to my original function')
        fun()
    return wrapper

@decorator
def greeting():
    print('Hello!')

greeting()