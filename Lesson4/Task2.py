phone_number = input('Введіть ваш номер телефону: ')
if  len(phone_number) != 10 or not phone_number.isdigit() :
    print('Номер не валідний')
else:
    print('Номер валідний')