with open('words.txt', 'r') as fd:
    word_list = fd.read().split()


def is_abecedarian(word):
    return word == ''.join(sorted(word))

words = [word for word in word_list if is_abecedarian(word)]

print ("There are {} abecedarian words.".format(len(words)))

def rec_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return rec_abecedarian(word[1:10])


rec_abecedarian(word_list)


def loop_abecedarian(word):
    i = 0
    while i < len(word)-1:
        if word[i+1] < word[i]:
            return False
        i = i+1
    return True

loop_abecedarian(word_list)