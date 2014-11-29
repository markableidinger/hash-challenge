import datetime

day_dict = {
    5: 'Friday',
    6: 'Saturday',
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday'
}

comp_dict = {
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday'
    }

def is_leap_year(year):
    leap = False
    if year % 4 == 0:
        leap = True
    if year % 100 == 0:
        leap = False
    if year % 400 == 0:
        leap = True
    return leap

def find_day(year, month, day):
    '''Returns the day of the week based on the year, month, and day entered.
    Raises errors if invalid year, month, or day number is entered.
    Assumes that the input will be all integers.'''
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year < 1:
        raise ValueError('Stick with AD, hotshot.')
    if 1 > month or 12 < month:
        raise ValueError('That month doesn\'t exist. Sorry!')
    if day > months[month - 1] or day < 1:
        if month == 2 and day == 29 and is_leap_year(year):
            pass
        else:
            raise ValueError('That day isn\'t in that month')
    leap_years_past = ((year - 1) // 4) - ((year - 1) // 100) + ((year - 1) // 400)
    year_days = ((year - 1) * 365) + leap_years_past
    print leap_years_past
    month_days = 0
    for i in range(month - 1):
        month_days += months[i]
    if is_leap_year(year) and month > 2:
        month_days += 1
    days_from_zero = year_days + month_days + day
    return day_dict[days_from_zero % 7]

if __name__ == '__main__':
    passing = True
    for year in range(1, 2001):
        for month in range(1, 13):
            for day in range(1, 29):
                if comp_dict[datetime.date(year, month, day).weekday()] == find_day(year, month, day):
                    print (year, month, day)
                else:
                    passing=False
                    break
    if passing:
        print('cool')
    else:
        print('nope')
