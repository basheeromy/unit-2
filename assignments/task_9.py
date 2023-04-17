# Write a function to generate all prime numbers up to a given limit

def prime_numbers(limit):
    for i in range(2,limit+1):
        prime = True
        for j in range(2,int((i/2)+1)):
            if i % j == 0:
                prime = False
                break
        if prime:
            print(i)
            
value = int(input("Enter the limit : "))
prime_numbers(value)