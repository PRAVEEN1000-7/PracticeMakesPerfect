import os

print(os.getcwd()) # get current working directory

os.chdir("E:/path/foldername") # change directory

print(os.listdir()) # List everything in current directory

print(os.listdir("E:/path/foldername")) # List a specific folder

os.mkdir("new_folder") # create folder
os.makedirs("a/b/c") # create nested folders
os.rmdir("new_folder") # remove empty folder


print(os.listdir(path='.')) # # List contents of a directory (files & folders)

os.rename("samplefile.txt","pytorch_info.txt")  # Rename/move a file

print(os.path.exists("PasswordGenerator.py"))  # Check if file/folder exists

print(os.path.isfile("file.txt"))       # Check if it's a file

print(os.path.isdir("folder"))          # Check if it's a folder

os.environ.get("PATH")   # Get PATH

# Directory Tree Traversal
for root, dirs, files in os.walk(os.getcwd()):
    print(root," =>", files)

