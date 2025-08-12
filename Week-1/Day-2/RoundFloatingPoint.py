# Q : Accept a float and round it to 2 decimal places.

number = float(input("Enter the number :"))
# By string formatting
print(f"Rounded Value of {number} with 2 decimal places by string formatting : {number:.2f}")
# By using round function
print(f"Rounded Value of {number} with 2 decimal places by round function : {round(number,2)}")