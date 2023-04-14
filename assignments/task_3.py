# Write a function to sort a array in ascending order

def tosort(slist,b):
    print(b)
    b = 20
    print(b)
    length = len(slist)
    for i in range(length-1):
        for j in range(i+1,length):
            if mylist[i] > mylist[j]:
                mylist[i],mylist[j] = mylist[j],mylist[i]  
        
a = 10         
mylist = [1000,0,54,6,0,4,38,29,100]
tosort(mylist,a)
print(mylist)
print(a)