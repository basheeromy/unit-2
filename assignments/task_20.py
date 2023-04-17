# Write a program to count the number of vowels in a given string.

while True:
    try:
        word = input("Enter the word to count vowels : ")
    except ValueError:
        print("Enter a word ")
    if word == '':
        print("Enter a word")
    elif word != '':
        break
count = 0 
for i in word:
    if i in "aeiouAEIOU":
        count += 1
        
print(f"Number of vowels in given word is : {count}")