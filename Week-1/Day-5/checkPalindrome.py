# Q : Check if a string is a palindrome.

word = input("Enter the word to check whether it's a palindrome :")

if word == word[::-1]:
    print("it is a palindrome.")
else:
    print("it is not a palindrome.")