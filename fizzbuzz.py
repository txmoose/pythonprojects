#!/usr/bin/env python
"""
Author:     Kyle Brieden
Date:       31 Jan 14
Updated:    31 Jan 14
Purpose:    practice problem - Fizz Buzz

Prompt:     Write a program that accepts a number from the user with proper
            input validation and will print numbers from 1 up to the input
            number replacing numbers that are divisible by 3 with fizz, numbers
            that are divisible by 5 with buzz, and numbers that are divisible
            by both 3 and 5 with fizzbuzz.
"""

import argparse


def get_valid_input():
    while True:
        number = raw_input('Integer to count to: ')

        if number.isdigit() and int(number) >= 1:
            break
        else:
            print 'Please enter a valid integer.\n'

    return int(number)


def check_value(x):
    if x % 3 == 0 and x % 5 == 0:
        return 'fizzbuzz'
    elif x % 3 == 0:
        return 'fizz'
    elif x % 5 == 0:
        return 'buzz'
    else:
        return x


def main():
    parser = argparse.ArgumentParser(description='Count up to specified'
                                     ' integer, replacing all numbers '
                                     'divisible by 3 with \"Fizz\", all '
                                     'numbers divisible by 5 with \"Buzz\",'
                                     ' and all numbers divisible by 3 and 5 '
                                     'with \"Fizzbuzz\".')
    parser.add_argument('-n', '--number', type=int, help='Number to count to',
                        dest='X')
    args = parser.parse_args()

    if not args.X:
        top_value = get_valid_input()
    else:
        top_value = args.X

    for x in range(1, top_value + 1):
        print check_value(x)


if __name__ == '__main__':
    main()
