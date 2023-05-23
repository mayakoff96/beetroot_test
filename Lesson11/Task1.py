with open('myfile.txt', 'w') as file:
    file.write('Hello file world!''\n')

with open('myfile.txt', 'r') as file_1:
    result = file_1.readlines()

print(result)

# Можемо додати відносний  шлях до файлу від поточної робочої директорії чи використати абсолютний
# 'Lesson11/myfile.txt'
# '/home/dmytro/beetroot_test/Lesson11/myfile.txt'