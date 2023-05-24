#1
numbers = (1, 3, 5, 7, 9, 11, 13, 15) # кортеж з числами

n = int(input("Введіть число n: ")) # користувач вводить число n

result = [num for num in numbers if num < n] # генератор списків, щоб створити новий список result, який містить всі числа з кортежу, які менші за n

print("Числа, які менші за", n, ":", result) # виводимо на екран всі числа, які менші за n

#2
# Створюємо кортеж з трьох рядків
my_tuple = ('melon', 'pineapple', 'orange')

# З'єднуємо рядки з комою як роздільником за допомогою методу join()
result = ','.join(my_tuple)

# Виводимо результат на екран
print(result)

#3
# Створюємо словник з інформацією про книги
books = {
    '1984': ('Джордж Орвелл', 1949, 328),
    'Лицар свободи': ('Джохар Дудаєв', 2020, 220),
    'Полум`яний бог': ('Ребекка Куанг', 2023, 584),
    'Код да Вінчі': ('Ден Браун', 2017, 592),
    'Старий і море': ('Ернест Хемінгуей', 1974, 571),
}

# Запитуємо в користувача назву книги
book_name = input('Введіть назву книги: ')

# Виводимо інформацію про книгу, якщо така є в словнику
if book_name in books:
    book_info = books[book_name]
    print(f'Автор: {book_info[0]}')
    print(f'Рік видання: {book_info[1]}')
    print(f'Кількість сторінок: {book_info[2]}')
else:
    print('Книга не знайдена в бібліотеці')

#4
students = {
    "Стефанчук": (15, "Чоловік", "Право"),
    "Максимова": (21, "Жінка", "Геологія"),
    "Антипов": (17, "Чоловік", "Механіка"),
    "Кіщук": (19, "Жінка", "Програмування")
}

name = input("Введіть прізвище студента: ")

if name in students:
    age, gender, major = students[name]
    print(f"Студент: {name}")
    print(f"Вік: {age}")
    print(f"Стать: {gender}")
    print(f"Факультет: {major}")
else:
    print("Такого студента не знайдено.")

#5
contacts = {
    'Dante Angelo': ['432896', '731946'],
    'Edward Kenway': ['167942', '287349', '719420'],
    'Hosea Matthews': ['831675']
}


def add_phone_number(contact_name, phone_number):
    if contact_name in contacts:
        contacts[contact_name].append(phone_number)
    else:
        contacts[contact_name] = [phone_number]


# Додавання нового номеру телефону до контакту
add_phone_number('Jacob Frye', '428562')

# Виведення списку номерів телефонів для всіх контактів
for contact, phone_numbers in contacts.items():
    print(contact + ': ' + ', '.join(phone_numbers))


