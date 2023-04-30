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

while i < len(random_list_1):
    if random_list_1[i] in random_list_2 and random_list_1[i] not in list_of_random_lists:
        list_of_random_lists.append(random_list_1[i])
    i += 1
print("Common integers: ", list_of_random_lists)

