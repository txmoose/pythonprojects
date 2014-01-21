#!/usr/bin/env python
"""Learning to use argparse"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,  
                    help="Echos the string presented in this position")
parser.add_argument("-v", "--verbosity", default=0,
        help="increases output verbosity", action="count")
args = parser.parse_args()

answer = args.square**2

if args.verbosity >= 2:
    print "The square of {} equals {}".format(args.square, answer)
elif args.verbosity >= 1:
    print "{}^2 == {}".format(args.square, answer)
else:
    print answer

