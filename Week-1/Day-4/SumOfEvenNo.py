# Q : Sum of all even numbers from 1 to 100.

sum=0
for i in range ( 1,101):
    sum+= i if (i&1==0) else 0
print(sum)