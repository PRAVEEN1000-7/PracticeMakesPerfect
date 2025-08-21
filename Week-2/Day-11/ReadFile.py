# Q : Read a text file and count the number of lines, words, and characters.

lines_count = words_count = char_count = 0

with open("sample.txt",'r') as file:
    for line in file:
        print(line)
        lines_count+=1
        words_count+=len(line.split())
        char_count+=len(line)
    
print("".center(20,"="))
print(f"Lines count :{lines_count:>5}")
print(f"Words count :{words_count:>5}")
print(f"Char count  :{char_count:>5}")
print("".center(20,"="))
