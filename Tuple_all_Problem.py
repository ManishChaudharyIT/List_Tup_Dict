# This is also the collection of diffrent-different types of data but the list is muttable and tuple is not
# here are some important tuple method 

#Python has two built-in methods that you can use on tuples.
'''Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found'''
# for coutn()
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

#for index()
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)