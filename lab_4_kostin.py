import time

#1
print("Завдання 1")

n = int(input("Введіть число: "))
print(n >= 100)

#2
print("Завдання 2")

n1 = float(input("Введіть перше число: "))
n2 = float(input("Введіть друге число: "))

if n1 < n2:
    print("число 1 < чмсло 2")
else:
    print("число 1 > чмсло 2")

#3
print("Завдання 3")

sp = input("What is the best plant in the world? \n")

if sp == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif sp == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not ", sp, "!")

#4
print("Завдання 4")

income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = (income / 100) * 18 - 556.02
else:
    tax = 14839.02 + (((income - 85528) / 100) * 32)
if tax < 0:
    tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

#5
print("Завдання 5")

year = int(input("Enter year: "))

if year < 1582:
    print("Not within the Gregorian calendar period.")
else:
    if year % 4 != 0:
        print("Its Common year")
    else:
        if year % 100 != 0:
            print("Its Leap year")
        elif year % 400 != 0:
            print("Its Common year")
        else:
            print("Its Leap year")

#6
print("Завдання 6")

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
+================================+
""")
while 1:
    number = int(input("Enter secret number: "))
    if number != secret_number:
        print("Ха-ха! Ви застрягли у моїй петлі!")
    else:
        print("Молодець, магле! Тепер ти вільний")
        break

#7
print("Завдання 7")

for i in range(5):
    print(i + 1, " Mississippi")
    time.sleep(1)
print("Ready or not, here I come!")

#8
print("Завдання 8")

while 1:
    word = (input("enter word: "))
    if word != "chupacabra":
        break
print("You've successfully left the loop.")

#9
print("Завдання 9")

user_word = input("Введіть слово: ")
user_word = user_word.upper()

for i in range(len(user_word)):
    if user_word[i] == "A":
        continue
    elif user_word[i] == "O":
        continue
    elif user_word[i] == "I":
        continue
    elif user_word[i] == "U":
        continue
    elif user_word[i] == "E":
        continue
    print(user_word[i])

#10
print("Завдання 10")

word_without_vowels = ""
user_word = input("Введіть слово: ")
user_word = user_word.upper()

for i in range(len(user_word)):
    if user_word[i] == "A":
        continue
    elif user_word[i] == "O":
        continue
    elif user_word[i] == "I":
        continue
    elif user_word[i] == "U":
        continue
    elif user_word[i] == "E":
        continue
    word_without_vowels += user_word[i]
print(word_without_vowels)

#11
print("Завдання 11")

block = int(input("Enter number of вricks: "))
height = 0
count = 1
while count <= block:
    block -= count
    count += 1
    height += 1
print("The height of the pyramid: ", height)

#12
print("Завдання 12")
step = 0
while 1:
    c0 = int(input("Введіть не від’ємне число:"))
    if c0 <= 0:
        print("Число неправильне! Повторіть знову!")
    else:
        break
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2
    else:
        c0 = 3 * c0 + 1
    print(int(c0))
    step += 1
print("steps =", step)
