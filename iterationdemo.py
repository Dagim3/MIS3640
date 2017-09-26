result = 1

for i in range (1):    
    result = result * (i + 1)
    print ('in the {}th iteration, new result = {}'. format (i,result))

print (result)
 

result = 0

for i in range (0, 1001, 2):
    result = result + i

print (result)

for i in ('dagim'):
    print (i)

import time
def countdown (n):
    while n>0:
        print(n)
        time.sleep(1)
        n=n-1
    print ('Offset!')

countdown (3)

iteration = 0
count = 0

for letter in 'hello, world':
    count += 1

print (count)

name = 'babson'
count = 0
for letter in name:
    if letter == "B" or 'b':
        count += 1

print (count)

mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
print(mysum)