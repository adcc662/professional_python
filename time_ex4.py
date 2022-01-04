from datetime import datetime
#In this program strftime transform to one string format the datetime format
my_datetime = datetime.now()
print(my_datetime)

my_str = my_datetime.strftime("%d/%m/%Y")
print(f'Formato LATAM: {my_str}')

my_str = my_datetime.strftime("%m/%d/%Y")
print(f'Formato USA: {my_str}')

my_str = my_datetime.strftime('We are in the year %Y')
print(f'Formato random: {my_str}')
