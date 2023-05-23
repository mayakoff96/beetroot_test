import json


def load_phonebook():
    try:
        with open('phonebook.json') as file:
            phonebook = json.load(file)
    except FileNotFoundError:
        phonebook = []

    return phonebook


def save_phonebook(phonebook):
    with open('phonebook.json', 'w', encoding='utf-8') as file:
        json.dump(phonebook, file, indent=4, ensure_ascii=False)


def add_contact():
    name = input("Введіть ім'я: ")
    surname = input("Введіть фамілію: ")
    full_name = f"{name} {surname}"
    phone_number = input("Введіть номер телефону: ")
    city = input("Введіть місто: ")
    country = input("Введіть країну: ")

    contact = {
        'name': name,
        'surname': surname,
        'full_name': full_name,
        'phone_number': phone_number,
        'city': city,
        'country': country
    }

    phonebook = load_phonebook()
    phonebook.append(contact)
    save_phonebook(phonebook)
    print("Контакт успішно доданий!")


def search_by_name(name):
    phonebook = load_phonebook()
    found_contacts = []
    for contact in phonebook:
        if contact['name'] == name:
            found_contacts.append(contact)

    return found_contacts


def search_by_surname(surname):
    phonebook = load_phonebook()
    found_contacts = []
    for contact in phonebook:
        if contact['surname'] == surname:
            found_contacts.append(contact)

    return found_contacts


def search_by_full_name(full_name):
    phonebook = load_phonebook()
    found_contacts = []
    for contact in phonebook:
        if contact['full_name'] == full_name:
            found_contacts.append(contact)

    return found_contacts


def search_by_phone_number(phone_number):
    phonebook = load_phonebook()
    found_contacts = []
    for contact in phonebook:
        if contact['phone_number'] == phone_number:
            found_contacts.append(contact)

    return found_contacts


def search_by_location(location):
    phonebook = load_phonebook()
    found_contacts = []
    for contact in phonebook:
        if contact['city'] == location or contact['country'] == location:
            found_contacts.append(contact)

    return found_contacts


def delete_contact(phone_number):
    phonebook = load_phonebook()
    updated_phonebook = [contact for contact in phonebook if contact['phone_number'] != phone_number]
    save_phonebook(updated_phonebook)
    print("Контакт успішно видалений!")


def update_contact(phone_number):
    phonebook = load_phonebook()
    for contact in phonebook:
        if contact['phone_number'] == phone_number:
            new_name = input("Введіть нове ім'я: ")
            new_surname = input("Введіть нову фамілію: ")
            new_full_name = f"{new_name} {new_surname}"
            new_phone_number = input("Введіть новий номер телефону: ")
            new_city = input("Введіть нове місто: ")
            new_country = input("Введіть нову країну: ")

            contact['name'] = new_name
            contact['surname'] = new_surname
            contact['full_name'] = new_full_name
            contact['phone_number'] = new_phone_number
            contact['city'] = new_city
            contact['country'] = new_country

            save_phonebook(phonebook)
            print("Контакт успішно оновлений!")
            return

    print("Контакт з таким номером телефону не знайдений.")


def main():
    options = {
        "1": add_contact,
        "2": lambda: search_contacts(search_by_name),
        "3": lambda: search_contacts(search_by_surname),
        "4": lambda: search_contacts(search_by_full_name),
        "5": lambda: search_contacts(search_by_phone_number),
        "6": lambda: search_contacts(search_by_location),
        "7": lambda: search_contacts(delete_contact),
        "8": lambda: search_contacts(update_contact),
    }

    while True:
        print_options()
        choice = input("Виберіть опцію: ")

        if choice == "9":
            print("До побачення!")
            break

        action = options.get(choice)
        if action:
            action()
        else:
            print("Невірний вибір. Спробуйте ще раз.")


def print_options():
    print("1. Добавити новий контакт")
    print("2. Пошук за ім'ям")
    print("3. Пошук за фамілією")
    print("4. Пошук за повним ім'ям")
    print("5. Пошук за номером телефону")
    print("6. Пошук за містом або країною")
    print("7. Видалити контакт за номером телефону")
    print("8. Оновити контакт за номером телефону")
    print("9. Вихід")


def search_contacts(search_func):
    search_term = input(f"Введіть {get_search_term_description(search_func)} для пошуку: ")
    found_contacts = search_func(search_term)
    print_found_contacts(found_contacts)


def get_search_term_description(search_func):
    descriptions = {
        search_by_name: "ім'я",
        search_by_surname: "фамілію",
        search_by_full_name: "повне ім'я",
        search_by_phone_number: "номер телефону",
        search_by_location: "місто або країну",
    }
    return descriptions.get(search_func, "")


def print_found_contacts(contacts):
    if contacts:
        for contact in contacts:
            print("==============================")
            print(f"Ім'я: {contact['name']}")
            print(f"Фамілія: {contact['surname']}")
            print(f"Повне ім'я: {contact['full_name']}")
            print(f"Номер телефону: {contact['phone_number']}")
            print(f"Місто: {contact['city']}")
            print(f"Країна: {contact['country']}")
            print("==============================")
    else:
        print("Контакти не знайдені.")


main()
