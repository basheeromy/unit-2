# Write a function to calculate the sum of all even numbers between 1 and n.

def evensum(limit):
    value = 0
    for i in range (2,limit,2):
        value += i
    return(value)

limit = int(input("Enter the limit : "))
print(evensum(limit))