# Write a program to find the sum of the digits of a given number.

number = input("Enter the number to find sum of the digits : ")
total = 0 
for i in number:
    total += int(i)
    
print(f"Result is : {total}")