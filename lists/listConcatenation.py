

# concatenation of two lists in python
list_1 = [1] * 8
list_2 = [2] * 8
list_3 = list_1 + list_2
print(list_3)

# we can do the same with the help of loops, 
# but the above given method is lot more easier

list_4 = [j for i in [list_1,list_2] for j in i]
print(list_4)

# we can achieve the same with extend() method also

list_1.extend(list_2)
print(list_1)

# we can achieve this in another way with '*' 
# this result will be with more 2s as we are already 
# assigned all values from list_2 to list_1 in above codes

list_5 = [*list_1,*list_2]
print(list_5)


# at last we can do list concatenation with the itertools.chain() method
import itertools
list_6 = list(itertools.chain(list_1,list_2))
print(list_6)