# Q : Sort a list without using sort().

lst = list(map(int,input("Enter the numbers (separated by comma(,)) :").split(',')))
print(f"The List : {lst}")

#insertion sort
for i in range(1,len(lst)):
    value_to_sort = lst[i]
    while lst[i-1]>lst[i] and i>0:
        lst[i-1],lst[i] = lst[i],lst[i-1]
        i-=1
        
print(f"The Sorted List : {lst}")



