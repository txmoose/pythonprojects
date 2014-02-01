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

import sys
import argparse

def get_valid_input_interactive():
    try:
        number = int(raw_input('Integer to count to: '))
    except:
        print 'Please restart the program and enter a valid integer.'
        sys.exit(-1)

    return number

def check_fizz(num):
    if num % 3 == 0:
        return True
    else:
        return False

def check_buzz(num):
    if num % 5 == 0:
        return True
    else:
        return False

def check_fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return True
    else:
        return False

def main():
    parser = argparse.ArgumentParser(description='Count up to specified'
            ' integer, replacing all numbers divisible by 3 with \"Fizz\"'
            ', all numbers divisible by 5 with \"Buzz\", and all numbers'
            ' divisible by 3 and 5 with \"Fizzbuzz\".')
    parser.add_argument('-n', '--number', type=int, help='Number to count to')
    args = parser.parse_args()

    if args.number == None:
        top_value = get_valid_input_interactive()
    else:
        top_value = args.number

    for x in range(1, top_value + 1):
        if check_fizzbuzz(x):
            print 'Fizzbuzz'
        elif check_fizz(x):
            print 'Fizz'
        elif check_buzz(x):
            print 'Buzz'
        else:
            print x

if __name__ == '__main__':

    main()
