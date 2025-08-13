# Q : Check if a year is a leap year.

year = int(input("Enter the year to check whether it's a leap year? :"))

if (year%4==0) and (year%100!=0) or (year%400==0):
    print(f"{year} is leap year.")
else:
    print(f"{year} is not a leap year")