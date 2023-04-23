def is_year_leap(year):
    if year < 1582:
        return False
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(year, month):
    month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year) and month == 2:
        return 29
    return month_length[month - 1]


def day_of_year(year, month, day):
    if month > 12 or month < 1:
        return None
    if day > days_in_month(year, month) or day < 1:
        return None

    total_days = day
    month = month - 1
    while month > 0:
        total_days = total_days + days_in_month(year, month)
        month -= 1

    return total_days


print(day_of_year(2001, 2, 29))
