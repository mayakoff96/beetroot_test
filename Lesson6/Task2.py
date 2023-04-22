from random import randint

random_list_1 = []
random_list_2 = []

while len(random_list_1) < 10 and len(random_list_2) < 10:
    random_list_1.append(int(randint(0, 10)))
print("Random list 1:", random_list_1)

while len(random_list_2) < 10:
    random_list_2.append(int(randint(0, 10)))
print("Random list 2:", random_list_2)

list_of_random_lists = []
i = 0

while i < 10:
    random_number = randint(0, 10)
    if random_number in random_list_1 and random_number not in list_of_random_lists:
        list_of_random_lists.append(int(random_number))
    elif random_number in random_list_2 and random_number not in list_of_random_lists:
        list_of_random_lists.append(random_number)
    i += 1
print("Common integers: ", list_of_random_lists)