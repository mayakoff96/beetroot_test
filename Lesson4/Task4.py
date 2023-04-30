name = 'dmytro'
inp_name = input('Enter your name: ')

if inp_name.lower() == name \
        or inp_name.upper() == name\
        or inp_name.capitalize() == name:
    print(True)
else:
    print(False)