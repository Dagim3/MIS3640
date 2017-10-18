names = ['Julian','Zach','Alex']
scores = [95,78,85]

grades = dict()
#grades['Zach'] = 75
#grades['Zach']
grades = {'Zach':75, 'Alex': 85, 'Julian': 95}
#print (grades)

def histogram(s):
    d = dict ()
    for c in s.lower():
        d[c]= d.get (c, 0) + 1
    return d

print(histogram('Bookbookkeeper'))