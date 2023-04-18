# Write a Python program to create a set and iterate over sets.

# program to create a string

length = int(input("Enter the length of set you would like to create : "))
set1 = set()

for i in range(length):
    while True: 
        try:
            value1 = input("Value : ")
        except ValueError:
            print("Input not valid  ")
        if value1 == "":
            continue
        else: 
            set1.add(value1)
            break

        
        
print(set1)
set2 = set()
for i in set1:
    set2.add(i)
    
print(set2)