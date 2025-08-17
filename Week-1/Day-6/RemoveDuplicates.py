# Q : Remove duplicates from a list (preserve order).

lst = input("Enter the list items (separated by (,) ) :").split(",")

unique_list=[]
for item in lst :
    if item not in unique_list:
        unique_list.append(item)

print("After removing duplicates : {}".format(unique_list))
