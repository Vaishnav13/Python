#Python - Remove List Items
#Remove "Banana"
thislist = ["Apple", "Banana", "Cherry"]
thislist.remove("Banana")
print(thislist)

#Remove the second item
thislist = ["Apple", "Banana", "Cherry"]
thislist.pop(2)
print(thislist)

#Remove the last item
thislist = ["Apple", "Banana", "Cherry"]
thislist.pop()
print(thislist)

#Remove the last item
thislist = ["Apple", "Banana", "Cherry"] 
thislist.pop(0)
print(thislist)

#Delete the entire list
thislist = ["Apple", "Banana", "Cherry"]
del thislist

#Clear the list content
thislist = ["Apple", "Banana", "Cherry"]
thislist.clear()
print(thislist)

