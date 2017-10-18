def isPalindrome(s):
    if str(s) == str(s)[::-1]: #This checks to see if the word is exactly the same backwords. (::-1) returns an inverse or flips the word
        return True #If true, return true

inputStr = input("Enter a string: ") #Enter any word
if isPalindrome(inputStr)== True: #If the isPalindrome function returned true, it will print 'That's a palindrome', if not it will print the opposite
    print("That's a palindrome.")
else:
    print("That isn't a palindrome.")
