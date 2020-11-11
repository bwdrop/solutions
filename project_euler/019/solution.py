#!/usr/bin/python3
"""
# Title
Counting Sundays

# URL
https://projecteuler.net/problem=19

# Problem
You are given the following information, but you may prefer to do some research for yourself.

-   1 Jan 1900 was a Monday.
-   Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
-   A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# Solved by
Heliane Ly
November 2020

# Algorithm
"""

def days_per_month_in(year):
    common_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
        return leap_year
    return common_year

sundays = 0
day = 1 # 1 Jan 1900 was a monday

for year in range(1900, 2001):
    month_list = days_per_month_in(year)
    for days_in_month in month_list:
        if day % 7 == 0 and year > 1900:
            sundays += 1
        day += days_in_month

print(sundays)