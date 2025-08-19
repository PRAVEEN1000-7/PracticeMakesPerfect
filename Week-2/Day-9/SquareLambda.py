# Q : Lambda function to square each number in a list.

lst = list(map(int,input("Enter the list numbers (separated by (,)) :").split(',')))

square = list(map(lambda x : x**2, lst))

print(square)