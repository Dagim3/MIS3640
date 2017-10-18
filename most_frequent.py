def most_frequent(s):
    """Sorts the letters in s in reverse order of frequency.
    s: string
    Returns: list of letters
    """
    import collections
    import string
    char_counter = collections.Counter(s)
    for char, count in char_counter.most_common():
        if char in string.ascii_lowercase:
            print(char, count)
        

s = input('Input a word:  ').lower()
most_frequent(s.lower())

def make_histogram(s):
    #"""Make a map from letters to number of times they appear in s.
    #s: string
    #Returns: map from letter to frequency
    #"""
    hist = {}
    hist = dict ()
    for x in s.lower():
        hist[x] = hist.get(x, 0) + 1
    return hist

s= input('Write a sentence:   ')
print (make_histogram(s))


def read_file(filename):
    f = open(filename,"r") #opens file with name of "test.txt"
    print(f.read())

read_file('trump_at_RNC.txt')

string = read_file('trump_at_RNC.txt')
letter_seq = most_frequent(string)
for x in letter_seq:
    print(x)