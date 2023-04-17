# Write a function to check given string is palindrome or not


def check_palindrome(string):
    limit = int((len(string)/2)+1)
    palindrome = True
    
    for i in range(1,limit):
        if string[i-1] != string[(i)*-1]:
            palindrome = False
            break
    
    return palindrome
    
word = input("Enter the word to check wether its a palindrome or not : ")

if check_palindrome(word):
    print("Given word is a palindrome")
else:
    print("Given word is not a palindrome")
    