# Q : Find the second largest number in a list.

lst = list(map(int,input("Enter the number separated by comma (,) : ").split(',')))

# insertion sort
for i in range(1,len(lst)):
    value_to_sort = lst[i]
    
    while lst[i-1]>lst[i] and i>0:
        lst[i-1],lst[i] = lst[i],lst[i-1]
        i-=1

# preserving only the unique elements
unique_list = []
for item in lst:
    if item not in unique_list:
        unique_list.append(item)

# 2nd largest number from the given list 
print("The Second Largest Number is : {} ".format(unique_list[-2]))