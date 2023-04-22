from random import randint

random_list = []

while len(random_list) < 10:
    random_list.append(randint(0, 50))

largest_number = random_list[0]
i = 1

while i < len(random_list):
    if random_list[i] > largest_number:
        largest_number = random_list[i]
    i += 1

print("Random list:", random_list)
print("Largest number:", largest_number)