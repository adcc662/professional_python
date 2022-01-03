import math 

def operations(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        exponent = math.exp(5)
        square = math.sqrt(9)
        print(f"The result of exponent is {exponent} and square is {square}")
    return wrapper



@operations
def logarithms(x:int):
    z = math.log(x)
    print(z)
logarithms(5)



