import re # імпорт модуля регулярних виразів для більш точної перевірки електренних адрес


class EmailValidation:

    def __init__(self, email):
        self.email = email
        self.validation()

    def validation(self):
        pattern = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$" # регулярний вираз для перевірки адреси
        if not re.match(pattern, self.email): # якщо email  не відповідає регулярному виразу
            raise ValueError('Invalid email address') # викликаємо помилку

    def __str__(self):
        return self.email

# mail = EmailValidation('asds1859@google.com')
# print(mail)


try:
    mail1 = "'email.valid1087@google.com'"
    mail1 = EmailValidation(mail1)
    print(f'Email {mail1} is valid.')
except ValueError:
    print(f'Email {mail1} is invalid.')

try:
    mail2 = "'invalid_email'"
    mail2 = EmailValidation(mail2)
    print(f'Email {mail2} is valid.')
except ValueError:
    print(f'Email {mail2} is invalid.')