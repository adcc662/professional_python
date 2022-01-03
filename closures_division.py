def make_division_by(n:int):
    """This closure returns a function that returns the division
     of an x number by n """
    def division(x:int):
        # assert n != 0 == int, "You can't divide by 0"
        return x / n
    return division 
     
division_by_3 = make_division_by(5)
print(division_by_3(21))

division_by_5 = make_division_by(5)
print(division_by_5(100))

division_by_18 = make_division_by(18)
print(division_by_18(54))