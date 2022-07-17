#Python - Change list items
#Change the second item
thislist = ["Apple", "Banana", "Cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change the values "Banana" and "Cherry" with the values "Blackcurrant" and "Watermelon"
thislist = ["Apple", "Banana", "Cherry", "Kiwi", "Melon", "Mango"]
thislist[1:3] = ["Blackcurrant", "Watermelon"]
print(thislist)

#Change the second value by replacing it with two new values
thislist = ["Apple", "Banana", "Cherry"]
thislist[1:2] = ["Blackcurrant", "Watermelon"]
print(thislist)

#Change the second and third value by replacing it with one value
thislist = ["Apple", "Banana", "Cherry"]
thislist[1:3] = ["Watermelon"]
print(thislist)

#Insert "Watermelon" as the third item
thislist = ["Apple", "Banana", "Cherry"]
thislist.insert(3, "Watermelon")
print(thislist)

#