s=[1,2,3,4]

for i in s:
    print(s)
    print('now we are removing',s.index(i))
    s.remove(i)
    print('after removing:',s)

for t in enumerate(s):
    print('index:',t[0], 'item: ',t)

       
      