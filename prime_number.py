def is_prime(number: int) -> bool:
    counter = 0
    list = [x for x in range(2,number) if number%x ==0]
    counter += 1
    return len(list) == 0



def run():
    number:int = 43
    # number = int(input('Please input a number: '))
    number_is_prime: bool = is_prime(number)
    print(f'{number} is a prime number? {number_is_prime}')

if __name__ == '__main__':
    run()
