# Q : Function to count occurrences of each character in a string (returns a dictionary).

def countChar(string):
    '''Function to count occurrences of each character in a string'''
    characters ={}
    for i in string:
        if i not in characters:
            characters[i]=1
        else:
            characters[i]+=1
    return characters

text = input("Enter the text :")

for key,value in countChar(text).items():
    print(f"{key:<3}:",value)