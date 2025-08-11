# Q : Convert between Celsius and Fahrenheit

choice = input("Convert from Celsius to Fahrenheit (C) or Fahrenheit to Celsius (F)? Enter C or F :")

if choice == "C":
    Celsius = float(input("Enter temperature in Celsius: "))
    Fahrenheit = ( 9 / 5 ) * Celsius + 32
    print(f"{Celsius}°C = {Fahrenheit}°F")

elif choice == "F":
    Fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    Celsius = ( 5 / 9 ) * ( Fahrenheit - 32)
    print(f"{Fahrenheit}°F = {Celsius}°C")

else :
    print("Invalid choice! Please enter C or F.")