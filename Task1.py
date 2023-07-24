# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            leap = year % 400 == 0
        else:
            leap = True
    else:
        leap = False

    print(f"{year} високосный год: {leap}")
    return leap


def is_valid_date(date_str):
    try:
        day, month, year = map(int, date_str.split('.'))
        if 1 <= year <= 9999 and 1 <= month <= 12:
            days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if is_leap_year(year):
                days_in_month[1] = 29
            return 1 <= day <= days_in_month[month - 1]
    except ValueError:
        pass
    return False



date_str = "34.12.2020"
result = is_valid_date(date_str)
print(f"Дата {date_str} существует: {result}")

