

# to initialize a string in python, we have three ways, 
# use single quotes, use double quotes, use tripple quotes
# use \ back slash as escaping key

caption = 'We are going to learn about strings in python.it\'s awesome\n '
print(caption)

sentence = "we can initialize string by using double quotes also, so we can use single quote ' without escape key\n"
print(sentence)

multi_line = """If we use tripple quote to intialize a string, we 
can make our long strings type in multi lines\n"""
print(multi_line)

multi_line = """If we use tripple quote to intialize a string, we \
can make our long strings type in multi lines, but by using a esaping back slash,
we can avoid this being multiline, here we can only see two lines as we use escaping key in first line\n"""
print(multi_line)

# string is immutable
# if we uncomment the following error, it will throw a type error as 'str' object does not support item assignment

# multi_line[2] = 's'

slicable = "letters inside a string can access by using indexing or slicing"
print(f"the first letter is : {slicable[0]}\n")
print(f"accessed letter by using negetive index : {slicable[-1]}\n")
print(f"slicing also possible to access data from string : {slicable[0:6]}\n")

reverse = "Hello World"
print(f"Reverse a string by using slicing and step index : {reverse[::-1]}\n")

print(f"acess data with slicing and step index : {reverse[::2]}\n")

spaces = "    with spaces    "
print(f"try to remove spaces from this string in next step :{spaces}\n")
print(f"use .strip method to remove spaces :{spaces.strip()}\n")

dupespace = spaces.strip()
print(f"{dupespace}\n")

# let's try more methods

# Use single quotes to give argument to .startwith() method

print(f"Variable reverse starts with H : {reverse.startswith('H')}\n")

# to convert string to upper case and lower case characters

convertion = "This works"
print(convertion.upper())
print(convertion.lower())
print(convertion.isupper())
print(convertion.islower())

# to find the index value of a particular letter present in the string, we can use find method
position = convertion.find('w')
print(f"positional value of 'w' in string is : {position}")

# we can also use find method to find substrings 
substring = convertion.find('work')
print(f"Positional value of substring 'work' starts : {substring}")

fake = convertion.find('p')
print(f".find method will return -1 if the given argument is not present in the string : {fake}\n")

mystring = "this strig is not so long"

# we can use .count() method to get count of a particular letter or word in a string
count = mystring.count('is')
print(f"count of 'is' in mystring is : {count}\n")


# use .replace method to replace a part of string with another one, we can't change 
# original one, but, we can make copy with change, print or re assign
print(mystring.replace('strig','string'))

# .split() method will help us to split a string in spaces and create a list 

to_split = "apple is a popular brand.apple products are best in class"
list_string = to_split.split()
print(list_string)

# to split string in anything else other than spaces, we have to pass the argument
# as shown bellow, the split point will be removed automatically

print(to_split.split('.'))
print(to_split.split('e'))

# to convert a list to string, we can't expect any spaces between elements from list.
# so, give in space at opening single quote (' '.join(mylist))
mylist = ['cat','is','a','domestic ','animal']
cat = ' '.join(mylist)
print(cat)

name = "Kannan"
salary = 50000
height = 5.687
intro = "%s is a react developer and he gets %d per month and he is %.2f feet tall "% (name,salary,height)
print(intro)

# Another way for string formatting 

details = {"name":"Risham","salary":50000,"height":4.789}

person = "{} is a mern stack developer and he gets {} and he is {:.2f} feet tall".format(details["name"],details["salary"],details["height"])
print(person)

# Another way is f"" string formatting
name1 = details["name"]
introduction = f"{name} and {name1} are mern stack developers and they get {salary} as salary per month and they are {height :.2f} "
print(introduction)