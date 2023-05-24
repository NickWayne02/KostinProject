def modul(num):
    if num < 0:
        return num * -1
    else:
        return num

print("Завдання 1")

def is_year_leap(year):
    if year < 1582:
        return False
    else:
        if year % 4 != 0:
            return False
        else:
            if year % 100 != 0:
                return True
            elif year % 400 != 0:
                return False
            else:
                return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
  yr = test_data[i]
  print(yr,"->",end="")
  result = is_year_leap(yr)
  if result:
      print("OK")
  else:
      print("Failed")

print("Завдання 2")

def days_in_month(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
       return 31
    elif month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    else:
        return 30


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
  yr = test_years[i]
  mo = test_months[i]
  print(yr, mo, "->", end="")
  result = days_in_month(yr, mo)
  print(result)

print("Завдання 3")

import datetime

def day_of_year(year, month, day):
    try:
        date = datetime.datetime(year=year, month=month, day=day)
        return date.timetuple().tm_yday
    except ValueError:
        return None
print(day_of_year(8,12,2002))

print("Завдання 4")

def is_prime(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    return flag

for i in range(1, 20):
   if is_prime(i + 1):
           print(i + 1, end=" ")
print()

print("Завдання 5")

def liters_100km_to_miles_gallon(liters):
    galon = liters / 3.785411784
    miles = 100_000 / 1609.344
    return miles / galon

def miles_gallon_to_liters_100km(miles):
    liters = 3.785411784
    kilometers = miles * 1609.344
    return liters / kilometers

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

print("Завдання 6")

def is_a_triangle(a, b, c):
    if modul(a - b) < c < a + b and modul(a - c) < b < a + c and modul(c - b) < a < c + b:
        return True
    else:
        return False

print(is_a_triangle(3, 3, 3))

print("Завдання 7")

def is_a_right_triangle(a, b, c):
    if is_a_triangle(a, b, c):
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
            return True
        else:
            return False
    else:
        return False

print(is_a_right_triangle(3,4,5))