# Q : Given a dictionary of students: marks, find the student(s) with the highest mark.

student = {}

size = int(input("Enter the number of students :"))
for i in range(1,size+1):
    name = input(f"Enter the student {i} name :")
    mark = float(input(f"Enter the student {i} mark :"))
    student[name] = mark
    
print("all students".center(30,'-'))

higher = max(student.values())
topper={}
for k,v in student.items():
    if v == higher:
            topper[k]=v
    print(f"{k} : {v}")


print("highest mark student".center(30,"-"))
for k,v in topper.items():
    print(f"{k} : {v}")
