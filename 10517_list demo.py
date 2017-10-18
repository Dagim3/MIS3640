AFC_east = ['New England Pats','Dolphins','Bills','Jets']
numbers = [42, 123]
empty = []

#print (AFC_east, numbers, empty)

AFC_east[3] = 'New York Giants'

print (AFC_east)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    
]

print(L[1][1])

numbers = [2, 0, 1, 6, 9]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    
print(numbers)

my_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]
print(len(my_list))

t = ['a','b','c','d','e']
print (t)

t.extend()
print(t)