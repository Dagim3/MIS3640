print ('Practice')
first_name = 'Dagim'
last_name = 'Girma'
fullname = first_name +" "+ last_name
print (fullname)
print ('Today is %2d-%02d.' % (9, 5))   
print ('Pi equals %.2f.' % 3.1415926)
print ('Age: %s. Gender: %s' % (20, "Male"))
print ('Growth rate: %d %%' % 7)
print ('3.14e-2 # Scientific notation')
print ('3.14e-2 # Scientific notation')
print ('123 + 222 # Integer addition')
print ('1.5 * 4 # Floating-point multiplication')
print ('2 ** 100 # 2 to the power 100')
print ('len(str(2 ** 1000000)) # How many digits in a really BIG number?')
import math
print(math.pi)
print(math.sqrt(85))
import time 
print(time.time())
current = time.time
print (time.time())
minutes = (time.time() % 60)
print (minutes)
print (time.localtime ())
def print_lyrics():
    print("Hey Jude. Don't make it bad")
    print("Take a sad song and make it better.")
    
type(print_lyrics())

def repeat_lyrics():
    print_lyrics()
    print ('Na - na - na - na - na, na - na - na - na')
    print_lyrics()

repeat_lyrics()

def print_twice(name):
    print(name)
    print(name)

print_twice('Dagim')
print(type(print_twice('name')))

my_name = 'Dagim'
print_twice (my_name)
print(type(print_twice))

open ('Python')