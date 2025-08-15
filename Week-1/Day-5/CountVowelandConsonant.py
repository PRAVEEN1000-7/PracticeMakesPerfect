# Q : Count vowels and consonants in a string.

text = input("Enter the text to count the vowels and consonants : ")

vowels=0
consonants=0

for i in text:
    if i.lower() in ['a','e','i','o','u']:
        vowels+=1
    elif i.isalpha() and i.lower() not in ['a','e','i','o','u']:
        consonants+=1

print(" Vowels and Consonants ".center(40,'-'))
print(f"\ttext      : {text}")
print(f"\tVowels    :{vowels:5}")
print(f"\tConsonant :{consonants:5}")
print(f"\tlen       :{len(text):5}")