def my_gen():
    """An example of generators"""
    
    print('Hello World')
    n = 0
    yield n

    print('Hello heaven')
    n = 1
    yield n

    print('Hello hell!')
    n = 2
    yield n

a = my_gen()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
StopIteration 