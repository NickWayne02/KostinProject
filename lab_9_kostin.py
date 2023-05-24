# 1
def mysplits(string):
    if not string.strip():
        return []

    words = string.split()
    return words


sentence1 = "To be or not to be, that is the question"
result1 = mysplits(sentence1)
print(result1)

sentence2 = "To be or not to be,that is the question"
result2 = mysplits(sentence2)
print(result2)

sentence3 = ""
result3 = mysplits(sentence3)
print(result3)

sentence4 = "abc"
result4 = mysplits(sentence4)
print(result4)

sentence5 = "   "
result5 = mysplits(sentence5)
print(result5)

# 2
number_dict = {'1': ('  #', '  #', '  #', '  #', '  #'),
               '2': ('###', '  #', '###', '#  ', '###'),
               '3': ('###', '  #', '###', '  #', '###'),
               '4': ('# #', '# #', '###', '  #', '  #'),
               '5': ('###', '#  ', '###', '  #', '###'),
               '6': ('###', '#  ', '###', '# #', '###'),
               '7': ('###', '  #', '  #', '  #', '  #'),
               '8': ('###', '# #', '###', '# #', '###'),
               '9': ('###', '# #', '###', '  #', '###'),
               '0': ('###', '# #', '# #', '# #', '###')}


def display_number(num):
    if num < 0:
        print("Число має бути невід'ємним.")
        return

    num_str = str(num)

    for level in range(5):
        for digit in num_str:
            if digit in number_dict:
                segments = number_dict[digit]
                print(segments[level], end=' ')
        print()


number_input = input('Введіть ціле число: ')
try:
    number = int(number_input)
    display_number(number)
except ValueError:
    print("Некоректне введення. Введіть ціле число.")


# 3
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            encoded = (ord(char) - base + shift) % 26 + base
            encoded_char = chr(encoded)
            result += encoded_char
        else:
            result += char

    return result


text = input("Введіть рядок, який треба зашифрувати: ")
shift = None

while True:
    shift_input = input("Введіть значення зсуву (ціле число з діапазону 1-25): ")
    try:
        shift = int(shift_input)
        if 1 <= shift <= 25:
            break
        else:
            print("Значення зсуву повинно бути в діапазоні 1-25.")
    except ValueError:
        print("Некоректне введення. Введіть ціле число.")

if shift is not None:
    encrypted_text = caesar_cipher(text, shift)
    print("Закодований текст:", encrypted_text)