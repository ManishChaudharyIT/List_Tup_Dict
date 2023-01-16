#Dictionary
'''Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.
Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
Duplicates Not Allowed
Dictionaries cannot have two items with the same key:
'''
#Note::As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
#Syntax
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# Here are different Method how can apply on dictionay
'''
Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

'''
print(len(thisdict))

print(type(thisdict))

x = thisdict.get("model")

x = thisdict.keys()

x = thisdict.values()

x = thisdict.items()

thisdict.update({"year": 2020})

thisdict.update({"color": "red"})

thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)


del thisdict["model"]
print(thisdict)

thisdict.clear()
print(thisdict)

mydict = thisdict.copy()
print(mydict)
#The dict() Constructor
'''It is also possible to use the dict() constructor to make a dictionary.
Example
Using the dict() method to make a dictionary:'''
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

