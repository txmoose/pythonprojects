#!/usr/bin/env python
"""
Author:     Kyle Brieden
Date:        3 Feb 14
Updated:     3 Feb 14
Purpose:    practice problem - Date Problem

Prompt:     Define two people and their birthdays.  Define a function that 
            will determine on which date the older of the two will be exactly
            twice as old, to the day, as the younger of the two.
"""


import datetime


def calc_2x_date(elder, junior):
    return junior + datetime.timedelta(days=((junior - elder).days))


def main():
    john = datetime.date(2003, 10, 19)
    sam  = datetime.date(1996,  7, 17)

    print calc_2x_date(sam, john)


if __name__ == '__main__':
    main()
