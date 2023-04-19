# The frozenset() function returns an immutable frozenset object 
# initialized with elements from the given iterable.

frozen = frozenset([1,2,3,4,'a','b','c'])
print(frozen)

a = frozenset([1,2,3,4,5,6,7])
b = frozenset([4,5,6,7,8,9,0])
print(f"union of a and b : {a.union(b)}" )

print(f"intersection of a and b : {a.intersection(b)}")

print(f"difference of a and b : {a.difference(b)}")

print(f"symmetric_difference of a and b : {a.symmetric_difference(b)}")

print(f"a and b don't have commen elements : {a.isdisjoint(b)}")

c = frozenset([4,5,6])
print(f"c is subset of b : {c.issubset(b)}")

print(f"b is superset of c : {b.issuperset(c)}")