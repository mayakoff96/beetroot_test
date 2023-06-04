import re # імпорт модуля регулярних виразів для більш точної перевірки електренних адрес


class EmailValidation:

    def __init__(self, email):
        self.email = email
        self.validation(self.email)

    def validation(self, email):
        pattern = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$" # регулярний вираз для перевірки адреси
        if not re.match(pattern, email): # якщо email  не відповідає регулярному виразу
            raise ValueError('Invalid email address') # викликаємо помилку

    def __str__(self):
        return f'{self.email}'

# mail = EmailValidation('asds1859@google.com')
# print(mail)


try:
    mail1 = EmailValidation('email.valid1087@google.com')
    print(f'Email {mail1} is valid.')
except ValueError:
    print(f'Email is invalid.')

try:
    mail2 = EmailValidation('invalid_email')
    print(f'Email {mail2}is valid.')
except ValueError:
    print(f'Email is invalid.')