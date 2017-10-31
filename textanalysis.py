print('Excercise 1')
from string import punctuation, whitespace

book = 'mobydick.txt'

with open(book, 'r') as fd:
    words = fd.read().split()

def clean(word):
    cleansed = ''
    for char in word:
        if ((char in punctuation) or (char in whitespace)):
            pass
        else:
            cleansed += char.lower()
    return cleansed
        
print (len([clean(word) for word in words]))

print('  ')
print('Excercise 2')
from string import punctuation, whitespace

mobydick = 'mobydick.txt'


def words(book):
    list_ = []
    flag = False
    signal = "*** START OF"
    for line in book:
        if flag == True:
            for word in line.split():
                list_.append(word)
        elif (signal in line) and (flag == False):
            flag = True
        else:
            pass
    return list_
    
def histogram(data):
    hist = {}
    for word in data:
        hist[word] = hist.get(word, 0) + 1
    return hist

books = [mobydick]

def stats():
    for book in books:
        book = open(book, 'r')
        print ("Stats for %s:" % book.name)
        data = [clean(word) for word in words(book)]
        book.close()
        print ("  Total: %s" % len(data))
        print ("  Unique: %s" % len(histogram(data)))
                
stats()

print('  ')
print('Excercise 3')
s = open('mobydick.txt','r').read() 

num_chars = len(s)

num_lines = s.count('\n')

words = s.split()
d = {}
for w in words:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

num_words = sum(d[w] for w in d)

lst = [(d[w],w) for w in d]
lst.sort()
lst.reverse()

print('\n The 30 most frequent words are ')

i = 1
for count, word in lst[:20]:
    print('%2s. %4s %s' %(i,count,word))
    i+= 1

from string import punctuation, whitespace

def clean(word):
    cleansed = ''
    for char in word:
        if ((char in punctuation) or (char in whitespace)):
            pass
        else:
            cleansed += char.lower()
    return cleansed

print('  ')
print('Excercise 4')
import sys, string
from collections import OrderedDict

def checkForWords(file):
    file = open('mobydick.txt')
    allWords = open('words.txt')
    dictionary = [line.rstrip('\r\n') for line in allWords] 
    for line in file.readlines():
        line = line.strip()
        words = line.split()
        for word in words:
            word = word[0:word.find(",")]
            found = False
            index = 0
            for element in dictionary:
                if found:
                    break
                if word == element:
                    found = True
                    break
                elif word != element and index < len(dictionary)-1:
                    index = index + 1
                else:
                    print ("The word " + word + " is not in the dictionary")
                    break

#checkForWords(open('mobydick.txt'))

print('  ')
print('Excercise 5')
def histogram(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

t = ['a', 'a', 'b']
hist = histogram(t)
print(hist)

def random_word(h):
    t = []
    for word, freq in h.items():
        t.extend([word] * freq)

    return random.choice(t)

