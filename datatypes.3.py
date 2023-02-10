# Dictionary ->{},key and values,mutable
mydic={
    "username":"mani",
    "Password":"1234",
    "Batch":2023,
}
print(mydic)


# Update
mydic["username"]=("mani123","mani")
print("The values after updating are",mydic)

mydic["Course"]="data science"
print("The values are",mydic)

list1=[2,4,6,8]
mydic["Password"]= list1
print("The values are",mydic)

mydic.pop("username")
print("The values are",mydic)

# updating the key
new=mydic["Course"]
del mydic["Course"]
mydic["Learning"]=new
print(mydic)