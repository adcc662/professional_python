def upper(func):
    def wrapper(text):
        return func(text).upper()
    return wrapper

@upper
def message(name):
    return f'{name} got a message'

print(message('Cesar'))