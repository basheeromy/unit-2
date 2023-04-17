# Write a program to find the sum of all the even or odd numbers below a given number.

def odd_sum(limit):
    total = 0 
    for i in range(1,limit+1,2):
        total += i 
    return total
        
        
def even_sum(limit):
    total = 0 
    for i in range(2,limit+1,2):
        total += i
    return total

choice = 0
while True:
    try:
        choice = int(input("Choose 1 for sum of odd numbers, 2 for even numbers : "))
    except ValueError:
            print("Please enter 1 or 2")
            continue
    if choice == 1 or choice == 2:
        break
    else:
        print("please enter 1 or 2")
limit = int(input("Enter the limit "))
if choice == 1:
    result = odd_sum(limit)
    print(result)
elif choice == 2:
    result = even_sum(limit)
    print(result)