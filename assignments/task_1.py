# find maximum element from an array.

numbers = [299,6,45,2,33,43,87,98,26,37]
max_el = numbers[0]
for i in numbers:
    if max_el < i:
        max_el = i
        
print(f"Maximum element in given array is : {max_el}")