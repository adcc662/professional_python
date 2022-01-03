def decorator(fun):
    def wrapper():
        print('This is added to my original function')
        fun()
    return wrapper

def greeting():
    print('Hello!')

greeting()
greeting = decorator(greeting)
greeting()