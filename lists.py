# Lists..They are used to store multiple items in a single variable.

# Example1
# Reverse a list in Python.

list = [2,3,4,5,6,7]
list.reverse()
print(list)

# Example2
# Turn every item of a list into square.
numbers = [5,10,15,20,25]
res = []
for i in numbers:
    res.append(i * i)
print(res)

# It could also be done this way;

number = [9,8,7,6]
pres = [x * x for x in number]
print(pres)

# Example3
# Concatenate two lists in the following order.
# list1 = ["Hello","take"],list2 = ["Dear","Sir"].

list1 = ["Hello","take"]
list2 = ["Dear","Sir"]
res = [x + y for x in list1 for y in list2]
print(res)

# Iterate both lists simultaneously.
# Given a two Python list. Write a program to iterate both lists simultaneously 
# and display items from list1 in original order and items from list2 in reverse order.

# The zip()function takes more 2 or more iterables like strings,dictionaries and tupples,
# aggaregates them in a tuple and returns it.

list3 = [90,80,70,60]
list4 = [900,800,700,600]

for x,y in zip(list3,list4[::-1]):
    print(x,y)

# Remove empty strings from a list of strings.
# We use a filter() function to remove the empty type from a list.

# Example4
# list5 = ["mangoes","oranges","kiwi","","pineapples"]
# pres = list(filter(None,list5))
# print(pres)

# Example5

# You have given a Python list. Write a program to find value 20 in the list,
# and if it is present, replace it with 200. Only update the first occurrence of an item.

# Replace list's item with new value if found.
#We Use list method index() to get the index of the number.

list6 = [20,40,67,47,3,8,0]
index = list6.index(20)
list1[index] = 200
print(list1)

# List length
mylist = ["volleyball","basketball","netball"]
print(len(mylist))

# A list can contain different data types
mylist1 = [2,3,4,5,6]
print(type(mylist1))

mylist2 = ["eat","live","learn","enjoy"]
print(type(mylist2))

