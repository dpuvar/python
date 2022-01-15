###         DICTIONARY           ###

# Write a Python script to check whether a given key already exists in a dictionary.
print("\n")
def check(dict, key):
     if key in dict.keys():
         print("available in dictionary", end=" ")
         print("value =", dict[key])
     else:
         print("not available in dictionary")
dict = {'q': 13, 't': 24, 'c': 36}
key = 't'
check(dict, key)
key = 'a'
check(dict, key)
print("\n")

# Write a Python script to merge two Python dictionaries.

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
print("the merged dictionary = ",(dict1| dict2))
print("\n")

#Write a Python program to sum all the items in a dictionary.

def returnSum(myDict):
    list = []
    for i in myDict:
        list.append(myDict[i])
    s = sum(list)
    return s
dict = {'a': 345, 'b': 560, 'c': 730}
print("Sum :", returnSum(dict))
print("\n")

#Write a Python script to add a key to a dictionary.

d = {'q':13, 'p':42}
print("before adding the key = ",d)
d.update({78:33})
print("after adding the key = ",d)
print("\n")

#Write a Python script to concatenate following dictionaries to create a new one.

dic1={'a':11, 2:22}
dic2={'c':23, 4:74}
dic3={5:65,'d':86}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print("the concatenated dictionary = ",dic4)
print("\n")



###         TUPLE           ###

#Write a Python program to create a tuple with different data types.

print("\n")
tuple = ('dhruv', True, 2.453, 3)
print(tuple)
print("\n")

#Write a Python program to create a tuple with numbers and print one item.

tuple = 1, 8, 5, 7, 240
print(tuple)
tuple = 8,
print("one item to be printed = ",tuple)
print("\n")

#Write a Python program to add an item in a tuple.

a_tuple = ("A1", "A2")
print("before adding item in tuple =",a_tuple)
new_tuple = "A3",
a_tuple = a_tuple + new_tuple
print("after adding item in tuple =",a_tuple)
print("\n")

#Write a Python program to convert a tuple to a string.

def convertTuple(tup):
    s = ''
    for item in tup:
        s = s + item
    return s
tuple = ('dh', 'ru', 'v ', 'pu', 'va','r')
s = convertTuple(tuple)
print("the coverted tuple to string is = ",s)
print("\n")

#Write a Python program to find the length of a tuple.

tuple = ('b','a','d','c')
print("the length of tuple = ",len(tuple))
print("\n")


###         SET           ###

#Write a Python program to add member(s) in a set and clear a set.

no_set = set()
print(no_set)
print("\nAdd single element:")
no_set.add(1)
print(no_set)
print("\nAdd multiple items:")
no_set.update([5, 8])
print(no_set)
print("\n")

#Write a Python program to remove an item from a set if it is present in the set.

num_set = set([10, 20, 30, 40, 50])
print("Original set elements:")
print(num_set)
print("\nRemove 10 from the said set:")
num_set.discard(10)
print(num_set)
print("\nRemove 50 from the said set:")
num_set.discard(50)
print(num_set)
print("\nRemove 40 from the said set:")
num_set.discard(40)
print(num_set)
print("\nRemove 20 from the said set:")
num_set.discard(20)
print(num_set)
print("\n")

#Write a Python program to create an intersection, Union, difference of sets.

A = {1, 2, 4, 6, 8}
B = {4, 8, 16, 40, 5}
print("Union :", A | B)
print("Intersection :", A & B)
print("Difference :", A - B)
print("\n")

#Write a Python program to find maximum and the minimum value in a set.

setv = {67, 50, 32, 135, 222, 230}
print("Original set elements:")
print(setv)
print("\nMaximum value :")
print(max(setv))
print("\nMinimum value :")
print(min(setv))
print("\n")

#Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

print("\n")

#most common from list

def most_common(List):
    return max(set(List), key = List.count)
List = [5, 1, 2, 5, 1, 5]
d=most_common(List)
print("the element = ",d," the repetition = ",List.count(d))
print("\n")

#most common from tuple

def most_common(List):
    return max(set(List), key = List.count)
List = list((2, 4, 7, 4, 5, 0, 3,))#converted tuple to list
d=most_common(List)
print("the element = ",d," the repetition = ",List.count(d))
print("\n")

#most common from dictionary

def most_common(List):
    return max(set(List), key = List.count)
dict={1:11,2:22,3:33,4:11,5:11}
List = list(dict.values())
d=most_common(List)
print("the element = ",d," the repetition = ",List.count(d))
