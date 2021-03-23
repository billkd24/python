#Lists -values that can be moded

fruits= ["Apple", "Mango", "Orange", "Peach", "Lemon", "Banana"]

#fetch values from the end of the list
#print (fruits[-1])

#assending order
#print (sorted(fruits))

#different way to sort
fruits.sort()

#traversing a list
for fruit in fruits:
    print(fruit)

    #adding something to the list
    #fruits.append("Avocado")

print (f"The list has {len(fruits)} fruits")

#check for a fruit in the list
fruit = "Tomato"
if not fruit in fruits:
    print (f"There is no {fruit} in the list")

#concatenate list
other_fruits = ["Passion", "Avocado"]

new_fruitlist = fruits + other_fruits

print (new_fruitlist)
#multiple the list
#print(new_fruitlist * 2)

    
#splice
#start at 1 and end at 5-1
print (new_fruitlist[1:5])

    