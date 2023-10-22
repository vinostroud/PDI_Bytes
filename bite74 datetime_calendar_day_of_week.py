from datetime import datetime


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    return date.strftime('%A')

dt = datetime(1979, 9, 21)
print(weekday_of_birth_date(dt))