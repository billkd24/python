#Sets a collection of unique values

#creating an empty set
my_set = set()

#adding values to a ser
my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add(6)
my_set.add(12)
my_set.add(2)
# in this case this will not be visible oon the out put my_set.add(2)

#print the elements
print(my_set)
print (f"The length of the set is {len(my_set)}")
#the dublicate 2 is not included in the length.

#remove items on the set
my_set.remove(6)
my_set.remove(1)
print(my_set)

print (f"The length of the set is {len(my_set)}")