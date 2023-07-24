
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



date_str = input("Введите дату в формате DD.MM.YYYY: ")
result = is_valid_date(date_str)
print(f"Дата {date_str} существует: {result}")
