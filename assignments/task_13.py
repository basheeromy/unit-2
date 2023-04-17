# Write a function to check if a given number is an Armstrong number.

def check_armstrong(number):
    length = len(str(number))
    computed = 0
    for i in str(number):
        computed += (int(i)**length)
    if number == computed:
        print("Given number is an Amstrong number") 
    else: 
        print("Given number is not an Amstrong number") 
     
nmb = int(input("Enter a number to check wether its an Amstrong number or not : "))   
check_armstrong(nmb)