""" 
    Write a program to find the sum of all the multiples of 3 or 5 
    below a given number.
"""

value = 0
while True:
    try: 
        value = int(input("Please enter 5 or 3 : "))
    except ValueError:
        print("Please enter 3 or 5 ")
        continue
    if value == 3 or value == 5:
        break
    else:
        print("value must be either 5 or 3")
        


limit = int(input("Please enter the limit : "))
result = 0 
for i in range(value,(limit+1),value):
    result += i
    
print(result)