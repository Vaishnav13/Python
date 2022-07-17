#Python - Add list items
#Using the append() method to append an item
thislist = ["Apple", "Banana", "Cherry"]
thislist.append("Orange")
print(thislist)

#Insert an item as the second position
thislist = ["Apple", "Banana", "Cherry"]
thislist.insert(1, "Orange")
print(thislist)

#Add the elements of tropical to thislist
thislist = ["Apple", "Banana", "Cherry"]
tropical = ["Mango", "Pineapple", "Papaya"]
thislist.extend(tropical)
print(thislist)

#Add elements of a tuple to a list
thislist = ["Apple", "Banana", "Cherry"]
thistuple = ["Kiwi", "Orange"]
thislist.extend(thistuple)
print(thislist)