#!/usr/bin/env python
"""
Author:     Kyle Brieden
Date:        1 Feb 14
Updated:     1 Feb 14
Purpose:    practice problem - Target Calculator

Prompt:     Write a function that accepts two arguments: A list of integers
            and a target value.  This function needs to perform calculations
            to verify whether or not two of the integers in the list are able
            to be added together to equal the target value.
"""


def get_valid_input():
    values = {}
    values['list'] = []
    while True:
        input_list = raw_input('Comma separated list of values: ').split(',')

        if all(x.strip().isdigit() for x in input_list):
            for x in input_list:
                values['list'].append(int(x))
            break
        else:
            print '\nPlease enter a list in this format: \"1, 2, 3, 4\"\n'

    while True:
        input_target = raw_input('Target integer: ').strip()

        if input_target.isdigit():
            values['target'] = int(input_target)
            break
        else:
            print '\nPlease enter an integer to target.'

    return values


def check_list(lst, tgt):
    answers = []
    for x in range(len(lst)):
        for y in lst[x:]:
            if lst[x] + y == tgt:
                answers.append('{} + {} = {}'.format(lst[x], y, tgt))
    if len(answers) == 0:
        answers.append('No values in the list can be added to '
                       'attain {}'.format(tgt))

    return answers


def main():
    values = get_valid_input()

    answers = check_list(values['list'], values['target'])
    for x in answers:
        print x

if __name__ == '__main__':
    main()
