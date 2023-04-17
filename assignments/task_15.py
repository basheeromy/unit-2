# Write a program to find the sum of all prime numbers up to a given limit. 

def prime_sum(limit):
    total = 0
    for i in range(2,limit+1):
        prime = True
        for j in range(2,int(i/2)+1):
            if i % j == 0:
                prime = False
                break
        if prime:
            total += i

    return total

limit = int(input("Enter the limit : "))
result =  prime_sum(limit)
print(f"Sum of all prime numbers in given limit is : {result}")