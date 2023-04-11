# to update an existing dictionary with new values and add new key value pairs, 
# we can use update() method.

student = {"name":"Nisam","place":"Areakode","domain":"mern"}
additional = dict(mob=9847877648,name = "Hisham",place="Koyilandy")
student.update(additional)
print(student)

# we can use unmutable data types like tuples as keys in dictionary
# use the bellow given syntax to create it

mytuple = (1,2,3)
sampledict = {mytuple:"tuple","lists":"notAceepted"}
print(sampledict)