from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " Segundos")
    return wrapper

@execution_time
#No positional parameters
def random_func():
    for _ in range(1, 100000000):
        pass

@execution_time
#Positional parameters
def addition(a:int, b:int) -> int:
    return a + b

#Named parameters o parametros nombrados
def greeting(name="Cesar"):
    print("Hello " + name)

addition(5,5)
random_func()
greeting("David")