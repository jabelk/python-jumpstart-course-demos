"""
Jump Start Python App 4 Journal
"""
__author__ = "Jason Belk"

import os

def print_header():
    header = "-" * 39
    app_name = "PERSONAL JOURNAL APP"
    app_space = " " * 10
    print(header)
    print(app_space + app_name + app_space)
    print(header)


def gather_commands():
    command = input("What do you want to do? [L]ist, [A]dd, or E[x]it? ")
    command = command.lower()
    return command


def list_entries(journal_entries):
    print("Your {} journal entries".format(str(len(journal_entries))))
    print(journal_entries)


def add_entries(journal_entries):
    journal_entries.append(input("Enter your journal Entry: "))


def main():
    journal_entries = []
    print_header()
    command = ""
    while command != "x":
        command = gather_commands()
        if 'l' in command:
            list_entries(journal_entries)
        elif 'a' in command:
            add_entries(journal_entries)
            pass
        else:
            "unknown command!"


main()
