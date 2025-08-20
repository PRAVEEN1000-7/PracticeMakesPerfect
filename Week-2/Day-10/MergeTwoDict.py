# Q : Merge two dictionaries.

dayscholar = {"ben":100,"gwen":90,"kevin":80}
hosteller = {"bruce":100,"stark":100,"steve":90}

#1.using update()
student = dayscholar.copy()
student.update(hosteller)
print(student)

#2.using dictionaries unpacking
student = {**dayscholar,**hosteller}
print(student)

#3.using | merge operator
student = dayscholar | hosteller
print(student)

