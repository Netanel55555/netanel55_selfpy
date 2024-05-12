import calendar
from datetime import datetime


def cal_day():

    date_input = input("Please enter a date: ")

    date = datetime.strptime(date_input, '%d/%m/%Y').date()

    weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    print(weekDays[date.weekday()])


while 1:
    cal_day()