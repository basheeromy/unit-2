"""
    The difference of two sets, written A - B is the set of all 
    elements of A that are not elements of B. The difference 
    operation, along with union and intersection, is an important and 
    fundamental set theory operation.
"""

a = {1,2,3,4,5,6,7,36,78}
b = {2,6,7,8,9,0,10}

# calculate difference of matrix a and b with the - operator 
c = a - b
print(c)

# calculate difference of matrix a and b with the .difference function

d = a.difference(b)
print(d)

# do the same with multiple sets (more than two sets)

e = {11,1,"w","c"}
f ={3,"d","e",1,"f"}

# with - operator
g = f - e - b - a
print(g)

# with .difference function

h = f.difference(e,b,a)
print(h)

# symmetric_difference
"""
    The symmetric_difference() method returns a set that contains
    all items from both set, but not the items that are present 
    in both sets. Meaning: The returned set contains a mix of 
    items that are not present in both sets.
"""

sa = {1,2,3,4,5,6,7}
sb = {1,8,0,11,21,30,2,6}
sd = {45,62,1,2,6,"a"}

# symmetric_difference function takes only one argument

sda = sa.symmetric_difference(sb)
print(f"Symmetric_differce is : {sda}")

sdb = sb.symmetric_difference(sa)
print(f"Symmetric_differce is : {sdb}")

# with operator instead of symmetric_difference funtion, we can use more than two sets to find symmetric_differece 

sbe = sa ^ sb  ^ sd
print(f"Symmetric_difference with ^ operator is : {sbe}")
