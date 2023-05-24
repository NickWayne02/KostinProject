#1
list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)
print("Завдання 1")
array = [1, 2, 3, 4, 5]
while 1:
    ch = int(input("Введіть номер елемента, який потрібно змінити (від 1 до 5): "))
    if ch >= 1 & ch <= 5:
        break
    else:
        print("Число не в діапазоні від 1 до 5. Повторіть спробу")
number = int(input("Введіть число, яке ви хочете змінити:"))

array[ch-1] = number

del array[-1]

print(array)

#2
print("Завдання 2")

array = [3, 8, 12, 1, 5, -1]

print(array)

for i in range(len(array) - 1):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)

#3
print("Завдання 3")

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

rep = []
for i in range(len(my_list)):
    if my_list[i] not in rep:
        rep.append(my_list[i])
my_list = rep[:]
print("The list with unique elements only:")
print(my_list)

#4
print("Завдання 4")

board = [["_"] * 8 for _ in range(8)]

board[0][0] = "R"
board[0][7] = "R"
board[7][0] = "R"
board[7][7] = "R"

for row in board:
    print(" ".join(row))