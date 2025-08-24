# Q : Word Frequency Counter – Reads a file, counts word occurrences, outputs top 10 most frequent words.

try :
    
    filename = input("Enter the file name (eg:sample.txt) :")
    occurence = {}
    with open(filename,'r') as file:
        content = file.read()
        
        for word in content.split():
            if word not in occurence:
                occurence[word] = 1
            else :
                occurence[word] +=1
        
        most_frequent = dict(sorted(occurence.items(), reverse=True, key=lambda x:x[1])[:10])

        for index, word in enumerate(most_frequent,start=1):
            print(f"{index}. {word} : {most_frequent[word]}")
        
        
except FileNotFoundError:
    print(f"ERROR : {filename} doesn't exists !")

except PermissionError:
    print(f"ERROR : {filename} doesn't have read permission!")

except Exception as e:
    print(f"ERROR : SOMETHING WENT WRONG !\n {e}")

