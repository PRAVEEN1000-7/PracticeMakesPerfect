from datetime import datetime, date

birthday = input("Enter the Date of Birth (yyyy-mm-dd) :")

birthday = datetime.strptime(birthday,"%Y-%m-%d").date()

today = date.today()
this_birthday = birthday.replace(year=today.year)

if this_birthday < today :
    this_birthday = this_birthday.replace(year=today.year +1)
    
daysleft = (this_birthday - today).days
print(f"🎂 Days till birthday: {daysleft} days")
