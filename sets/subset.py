# A set A is a subset of another set B if all elements of the 
# set A are elements of the set B. In other words, the set A is contained inside the set B. 

a = {1,2,3,4,5,6}
b = {1,2,3}
c = {4,5,6}

print(a.issubset(b))
print(b.issubset(a))
print(a.issubset({1,2,3,4,5,6,7,8}))

# we can also use <= operator to check a set is wether subset of another set or not
print(f"with <= operator : {(c <= a)}")

# A set is considered to be a subset of itself:

print(a.issubset(a))

"""
    A proper subset is the same as a subset, except that the sets can’t 
    be identical. A set x1 is considered a proper subset of another set 
    x2 if every element of x1 is in x2, and x1 and x2 are not equal.
"""
# while a set is considered a subset of itself, it is not a proper subset of itself.

d = {1,2,3,4,5,6,7}
e = {1,2,3,5}
f = {1,3,2,4,5,6,7}

print(f"c is a proper subset of d : {(c < d)}")

# A superset is the reverse of a subset. A set x1 is considered a 
# superset of another set x2 if x1 contains every element of x2.

print(f"d is a superset of e : {(d.issuperset(e))}")

print(f"d is a superset of e : {(d >= e)}")

# a set is considered as a superset of itself
print(f"a set is a superset of itsefl : {(d.issuperset(d))}")

# > operator checks wether a set is proper superset or not

print(f"d is proper superset of e : {d > e}")
