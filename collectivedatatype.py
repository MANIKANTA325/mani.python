# List -> collection od data, ordered ,its mutable ,[]
mylist=["mani","pavan","simple","when",255,False,325.63]
print("The value of mylist is",mylist)
print(type(mylist))
# Index value -> prints individual data
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[4])
print(mylist[5])
print(mylist[6])

# changeable
# Update
mylist[-2]=True
print("The updates values of list is",mylist)

# append(add)
mylist.append("hello",)
print("The values after adding are",mylist)

# insert
mylist.insert(3,"hai")
print("The value after indexing is",mylist)

list1=[5,45,562]

# extend
mylist.extend(list1)
# list1.extend(mylist)
print("The value of list is",mylist)

# Remove
mylist.remove(255)
print("The values are",mylist)

# delete
del mylist[-6]
print("The values after deleting is", mylist)

del mylist
print(mylist)