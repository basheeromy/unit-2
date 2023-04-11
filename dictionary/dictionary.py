# dictionary is another datatype in python and dictionary helps us to store data as key value pair
# the following are two ways to initialize a dictionary

student = {"name":"Rahul","place":"Kannur","state":"kerala","Mob":9847313208}

teachers = dict(name="Nasweef",place="Narikkuni",district="Kozhikode",state="Kerala",Mob=9847313208)

print(student)
print(teachers)

# dictionary is mutable, so to assign a new value
teachers["email"] = "nasweef@sample.com"
print(teachers)
# also we can over ride the value 
teachers["email"] = "nasweefnkn@sample.com"
print(teachers)
# to assign a particular value from dictionary to a variable
name = teachers["name"]
print(name)
# to delete an item from dictionary using pop method , pop need one argument
name1 = teachers.pop("name")
print(name1)
# to delete the last item from dictionary, popitem takes no argument
teachers.popitem()
print(teachers)
# to delete an item from dictionary with del method
del teachers["Mob"]
print(teachers)

# try and exception to handle error

try:
    print(teachers["email"])
except:
    print("this value does not exist.")
    
if "place" in teachers:
    print(teachers["place"])
    
# to iterate through keys in a dictionary

for key in teachers:
    print(key)

# to iterate through keys and values in a dictionary

for key, value in student.items():
    print(f"key = {key} : value = {value}")
    
# to get list of keys in python dictionary
print(list(teachers.keys()))

# same like we see with list, dictionary also stores only memory location in variable, 
# so, if we make change in copy, it will affect original one, so to get entirely different copy
# use copy method

student1 = student.copy()
student1["subject"] = "commerce"
print(student)
print(student1)

# also we can use dict function to create entirely new copy 

student2 = dict(student1)
student2.pop("state")
print(student1)
print(student2)