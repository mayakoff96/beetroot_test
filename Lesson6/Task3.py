list_1 = list(range(1, 101))
list_2 = []

i = 0

while i < len(list_1):
    if list_1[i] % 7 == 0 and list_1[i] % 5 !=0:
        list_2.append(list_1[i])
    i += 1

print(list_2)