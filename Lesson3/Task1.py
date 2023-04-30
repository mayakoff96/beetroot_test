from datetime import datetime
# Import the datetime module to use current day of the week.

day = datetime.today().strftime("%A")
name = "Dmytro"

print(f"Good day {name}! {day} is a perfect day to learn Python.")