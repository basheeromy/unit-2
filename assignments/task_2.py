# Write a function to reverse a string 

name = input("Enter a word to reverse : ")
name2 = ""
for i in range(len(name)):
    name2 += name[(-(i+1))]

print(name2)