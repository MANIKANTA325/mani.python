file=open("a.txt" ,"w")
file.write("This is written by the mani")

file=open("a.txt" ,"r")
print(file.read())
file=open("a.txt","a")
file.write("\nThis is written by the manikanta

file=open("a.txt" ,"r")
print(file.read())
with open("a.txt","r") as file1:
  print(file1.read())
