# Q : Write a program that copies content from one file to another.

# reading the file content
with open("sample.txt","r") as file:
    content = file.read()

#writing the content to the file
filename = "newfile.txt"
file = open(filename,"w")
file.write(content)
print("successfully written to the file : {}".format(filename))
file.close()
