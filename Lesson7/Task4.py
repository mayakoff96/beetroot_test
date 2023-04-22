# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
# Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,

list_days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_list_1 = {}

for i, day in (enumerate(list_days_of_the_week)):
    days_list_1[i + 1] = day
print(days_list_1)

# reversed_dict = {value: i for i, value in days_list_1.items()}
# print(reversed_dict)
reversed_dict = {}

for i, value in days_list_1.items():
    reversed_dict[value] = i
print(reversed_dict)