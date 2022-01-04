my_set = {1,2,3,4,5,6,7}
print(my_set)

#Delete an existing element
my_set.discard(1)
print(my_set)
#Delete an existing element
my_set.remove(2)
print(my_set)
#Delete a non existing element
my_set.discard(10)
print(my_set)
#Delete a non existing element
my_set.remove(12)
print(my_set)