old_str_1 = 'helloworld'
# Expected Result: 'held'
old_str_2 = 'my'
# Expected Result: 'mymy'
old_str_3 = 'x'
# Expected Result: 'Empty String'


if len(old_str_1) < 2:
    new_string_1 = ""
else:
    new_string_1 = old_str_1[:2] + old_str_1[-2:]
print(new_string_1)

if len(old_str_2) < 2:
    new_string_2 = ""
else:
    new_string_2 = old_str_2[:2] + old_str_2[-2:]
print(new_string_2)

if len(old_str_3) < 2:
    new_string_3 = ""
else:
    new_string_3 = old_str_3[:2] + old_str_3[-2:]
print(new_string_3)