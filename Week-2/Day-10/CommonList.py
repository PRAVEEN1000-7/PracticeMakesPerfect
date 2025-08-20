# Q : Find common elements between two lists using sets.

num1 = [1,2,3,4,5]
num2 = [5,7,4,3,7,5]

unique_combine_list = list( set(num1) & set(num2) )

print(unique_combine_list)