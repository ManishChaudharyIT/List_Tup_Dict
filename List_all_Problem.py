# List::List mean that it is a container/collection differrent data types.
# List has various function mean that what type of task we can perform on list
#Method	Description
'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''
# Here are example for how to define list in any data types
my_int_list=[1,2,3,4,5,6,6,767,3,34,56]
my_string_list=["Manish","Chaudhary","Rupali","Sharma","Karishma","Singh"]
my_float_list=[43.5,67.5,54.5,639.21,23.65]
mix_list=[123,453,"mansih",55.76,"chaudhary",897]

# Here are method how we can apply method on list "in this example i going to apply all method on my_int_list but you can apply on any list "
my_int_list.append(543)
print("\n",my_int_list)



my_int_list.copy()
print("\n",my_int_list)

my_int_list.count(6)
print("\n",my_int_list)

my_int_list.extend(my_float_list) #the my_float_list all values will be add in my_int_list
print("\n",my_int_list)

my_int_list.insert(5,562)
print("\n",my_int_list)

my_int_list.remove(34)
print("\n",my_int_list)

my_int_list.reverse()
print("\n",my_int_list)

my_int_list.sort()
print("\n",my_int_list)

my_int_list.clear()
print("\n",my_int_list)




