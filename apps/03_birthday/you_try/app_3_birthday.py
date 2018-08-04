"""
Jump Start Python App 3 Birthday
"""
__author__ = "Jason Belk"

import datetime


def print_header():
    header = "-" * 39
    app_name = "BIRTHDAY APP"
    app_space = " " * 10
    print(header)
    print(app_space + app_name + app_space)
    print(header)


def gather_facts():
    """
    ask user for bday
    :return: year, month, day - all integers
    """
    year = int(input("What year were you born [YYYY]? "))
    month = int(input("What month were you born [MM]? "))
    day = int(input("What day were you born [DD]? "))
    bday = datetime.date(year, month, day)

    return bday


def print_finish(bday, countdown):
    print("\nIt Looks like you were born on "
          + str(bday) + "\nLooks like your birthday is in "
          + str(countdown) + " days.\nHope you're looking forward"
                             " to it!")


def diff_between_dates(original_date, target_date):
    # taken from example
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)

    dt = this_year - target_date
    return dt.days


def main():
    today = datetime.date.today()

    print_header()

    bday = gather_facts()

    num_of_days = diff_between_dates(bday, today)

    # birthday in future
    # birthday today
    # birthday already past
    # logic
    print_finish(bday, num_of_days)


main()
