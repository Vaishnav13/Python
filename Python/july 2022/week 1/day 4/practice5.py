#Python - Loop Lists
#Print all the list item one by one
thislist = ["Apple", "Banana", "Cherry"]
for x in thislist:
    print(x)
    
#Print all items by referring to their index number
thislist = ["Apple", "Banana", "Cherry"]    
for i in range(len(thislist)):
    print(thislist[i])

#Print all items, using while loop to go through all the index numbers
thislist = ["Apple", "Banana", "Cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
    
#A short hand for loop that will print all items in a list
thislist = ["Apple", "Banana", "Cherry"] 
[print(x) for x in thislist]