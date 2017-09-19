age = input ('What is your age?')
age = int (age)

if age >= 18:
    print('Your age is{}.'.format(age))
    print('adult')
else:
    print ('Your age is {}.'.format(age))
    print ('Teenager')

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')