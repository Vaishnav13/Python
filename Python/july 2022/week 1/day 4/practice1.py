#Python - Access List items
#Print second item of a list
thislist = ["Apple", "Banana", "Cherry"]
print(thislist[2])

#Print last item of the list
thislist = ["Apple", "Banana", "Cherry"]
print(thislist[-3])

#Return third, fourth and fifth item
thislist = ["Apple", "Banana", "Cherry", "Kiwi", "Melon", "Mango"]
print(thislist[3:6])

#This example returns the items from "Cherry" to the end
thislist = ["Apple", "Banana", "Cherry", "Kiwi", "Melon", "Mango"]
print(thislist[2:])

#This example returns the items from "orange" (-4)to, but NOT including "mango" (-1)
thislist = ["Apple", "Banana", "Cherry", "Orange", "Kiwi", "Melon", "Mango"]
print(thislist[-4:-1])

#Check if "Apple" present in the list
thislist = ["Apple", "Banana", "Cherry", "Kiwi", "Melon", "Mango"]
if "Apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

