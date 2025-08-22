# Q : Handle file-not-found error gracefully.

try :
    filename = input("Enter the file name with format (eg:sample.txt) :")
    file = open(filename,"r")
    content = file.read()
    print(content)
    
except FileNotFoundError:
    print(f"ERROR : there is no file called {filename}")
    
except PermissionError:
    print(f"ERROR : you don't have permission to read this file!")
    
except Exception as e:
    print(f"ERROR : something went wrong !\n{e}")
    
finally :
    try:
        file.close()
    except NameError:
        pass