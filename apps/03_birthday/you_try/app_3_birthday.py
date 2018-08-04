"""
Jump Start Python App 3 Birthday
"""
__author__ = "Jason Belk"

header = "-"*39
app_name = "BITHDAY APP"
app_space = " "*10
print(header)
print(app_space+app_name+app_space)
print(header)
bday = ""
countdown = ""
year = input("What year were you born [YYYY]? ")
month = input("What month were you born [MM]? ")
day = input("What day were you born [DD]? ")
# logic
print("\nIt Looks like you were born on "
      + str(bday) + "\nLooks like your birthday is in "
      + str(countdown) + " days.\nHope you're looking forward"
                         "to it!")