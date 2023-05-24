import math

#1
print("Завдання 1")
x = input("Enter: ")
print(type(x))
# pi = 3.14
x = float(input("Enter x: "))
sigma = float(input("Enter o: "))
mu = float(input("Enter u: "))
f = (1 / sigma * (2 * math.pi) ** 0.5) * math.exp(-(((x - mu) ** 2 ) / (2 * sigma ** 2)))
print("f(x) = ", f)

#2
print("Завдання 2")

john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=" , ")

totalApple = john + mary + adam

print("Загальна кількість яблук: ", totalApple)

#3
print("Завдання 3")

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "миль", round(miles_to_kilometers, 2), "кілометрів")
print(kilometers, "кілометрів", round(kilometers_to_miles, 2), "миль")

#4
print("Завдання 4")

x = 0.
y = (3 * x ** 3) - (2 * x ** 2) + (3 ** x) - 1

print("x = 0 \ny = ", y)

x = 1.
y = (3 * x ** 3) - (2 * x ** 2) + (3 ** x) - 1

print("x = 1 \ny = ", y)

x = -1.
y = (3 * x ** 3) - (2 * x ** 2) + (3 ** x) - 1

print("x = -1 \ny = ", y)

#5
print("Завдання 5")
number_of_hours = 2
seconds_in_hour = 3600

print("Годин: ", number_of_hours)
print("Секунд в годинах: ", number_of_hours * seconds_in_hour)

print("Бувай")

#6
print("Завдання 6")

a = float(input("Введіть a: "))
b = float(input("Введіть b:"))

print("a + b = ", a + b)
print("a - b = ", a - b)
if b == 0:
    print("Не можна ділити на нуль")
else:
    print("a / b = ", a / b)
print("a * b = ", a * b)


print("\nThat's all, folks!")

#7
print("Завдання 7")

x = float(input("Enter value for x: "))
y = 1/(x + 1/(x + 1/(x + 1/(x + 1/x))))
print("y =", y)

#8
print("Завдання 8")

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

hour *= 60
hour += mins + dura
mins = hour % 60
hour = int(hour / 60)
hour = hour % 24

print(hour, ":", mins)





