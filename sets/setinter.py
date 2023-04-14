# set intersection in python 
# resultant set will contain elements present in all sets
# You can specify multiple sets with the intersection method 
# and operator, just like you can with set union:

a = {1,2,3,45,6}
b = {2,1,45,34}
c = {43,1,2,35}
d = {9,2,8,1}

e = a&b&c&d
print(f"itnersection of a,b,c,d computed with & operator is : {e}")

f = a.intersection(b,c,d)
print(f"itnersection of a,b,c,d computed with .intersection() method is : {f}")



