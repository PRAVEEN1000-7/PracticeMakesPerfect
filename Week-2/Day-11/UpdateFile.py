# Q : Append user input to an existing file.

with open("sample.txt","a") as file:
    text = input("Enter the text to update : ")
    file.write(text+'\n')
    
print("Your input has been added to sample.txt")
