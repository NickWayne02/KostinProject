#1
class Timer:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __str__(self):
        return f"{self.__format_time(self.__hour)}:{self.__format_time(self.__minute)}:{self.__format_time(self.__second)}"

    def __format_time(self, time):
        if time < 10:
            return f"0{time}"
        return str(time)

    def next_second(self):
        self.__second += 1
        if self.__second == 60:
            self.__second = 0
            self.__minute += 1
            if self.__minute == 60:
                self.__minute = 0
                self.__hour += 1
                if self.__hour == 24:
                    self.__hour = 0

    def previous_second(self):
        self.__second -= 1
        if self.__second == -1:
            self.__second = 59
            self.__minute -= 1
            if self.__minute == -1:
                self.__minute = 59
                self.__hour -= 1
                if self.__hour == -1:
                    self.__hour = 23


timer = Timer(23, 59, 59)
print(timer)

timer.next_second()
print(timer)

timer.previous_second()
print(timer)


#2
class WeekDayError(Exception):
    pass


class Weeker:
    def __init__(self, day):
        days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        if day not in days_of_week:
            raise WeekDayError("Invalid day of the week")
        self.day = day

    def __str__(self):
        return self.day

    def add_days(self, n):
        days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        current_index = days_of_week.index(self.day)
        new_index = (current_index + n) % 7
        self.day = days_of_week[new_index]

    def subtract_days(self, n):
        self.add_days(-n)


try:
    day1 = Weeker('Mon')
    print(day1)
    day1.add_days(3)
    print(day1)
    day1.subtract_days(2)
    print(day1)

    day2 = Weeker('Sat')
    print(day2)
    day2.add_days(1)
    print(day2)
    day2.add_days(7)
    print(day2)

    day3 = Weeker('Invalid')
    print("This line should not be printed")
except WeekDayError:
    print("Sorry, I can't serve your request.")

#3

from math import hypot


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


point1 = Point(1, 1)
point2 = Point(2, 2)

distance1 = point1.distance_from_point(Point(0, 0))
print(distance1)

distance2 = point2.distance_from_point(point1)
print(distance2)

#4

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, point1, point2, point3):
        self.points = [point1, point2, point3]

    def perimeter(self):
        side1 = self.distance(self.points[0], self.points[1])
        side2 = self.distance(self.points[1], self.points[2])
        side3 = self.distance(self.points[2], self.points[0])
        return side1 + side2 + side3

    def distance(self, point1, point2):
        return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)


# Створення об'єктів точок
point1 = Point(1, 0)
point2 = Point(1, 1)
point3 = Point(2, 0)

# Створення об'єкта трикутника
triangle = Triangle(point1, point2, point3)

# Обчислення периметру трикутника
perimeter = triangle.perimeter()

print("Периметр трикутника:", "{:.15f}".format(perimeter))