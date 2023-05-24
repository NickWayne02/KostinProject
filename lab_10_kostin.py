#1
def is_palindrome(text):
    text = text.replace(" ", "").lower()
    if text == text[::-1]:
        return True
    else:
        return False


user_text = input("Введіть текст: ")

if is_palindrome(user_text):
    print("Це паліндром!")
else:
    print("Це не паліндром.")


#2
def is_anagram(text1, text2):
    text1 = text1.replace(" ", "").lower()
    text2 = text2.replace(" ", "").lower()
    if len(text1) != len(text2):
        return False

    for char in text1:
        if char not in text2:
            return False

    return True


text1 = input("Введіть перший текст: ")
text2 = input("Введіть другий текст: ")

if is_anagram(text1, text2):
    print("Це анаграми!")
else:
    print("Це не анаграми.")


#3
def calculate_life_number(date):
    date = list(filter(str.isdigit, date))

    life_number = sum(int(digit) for digit in date)

    while life_number > 9:
        life_number = sum(int(digit) for digit in str(life_number))

    return life_number


birthdate = input("Введіть дату народження (у форматі РРРГММДД, або РРРРДДММ, або ММДДРРРР): ")

life_number = calculate_life_number(birthdate)

print(f"Цифра життя для дати {birthdate}: {life_number}")


#4
def is_hidden(word, combination):
    word = word.lower()
    combination = combination.lower()

    current_index = -1

    for char in word:
        current_index = combination.find(char, current_index + 1)

        if current_index == -1:
            return False

    return True


word = input("Введіть слово: ")
combination = input("Введіть комбінацію символів: ")

if is_hidden(word, combination):
    print("Yes")
else:
    print("No")


#5
def is_hidden(word, combination):
    word = word.lower()
    combination = combination.lower()

    current_index = -1

    for char in word:
        current_index = combination.find(char, current_index + 1)

        if current_index == -1:
            return False

    return True


try:

    word = input("Введіть слово: ")
    combination = input("Введіть комбінацію символів: ")

    if is_hidden(word, combination):
        print("Yes")
    else:
        print("No")
except Exception as e:
    print("Сталася помилка:", str(e))


#6
def get_integer_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if value < min_value or value > max_value:
                print(f"Error: the value is not within permitted range ({min_value}..{max_value})")
            else:
                return value
        except ValueError:
            print("Error: wrong input")


input_prompt = "Введіть ціле число: "
min_value = 1
max_value = 100

integer_value = get_integer_input(input_prompt, min_value, max_value)
print(f"Введене число: {integer_value}")