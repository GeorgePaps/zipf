"""
Counts the occurence of full stops, question marks 
and exclamation points and prints them on the screen.
"""

import sys
import argparse
import string
from collections import Counter


def main(args):
    """Count the occcurence of each word in a string"""
    text = args.infile.read()
    print(f"Number of . is {text.count('.')}")
    print(f"Number of ? is {text.count('?')}")
    print(f"Number of ! is {text.count('!')}")

        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type = argparse.FileType('r'), nargs='?',default = '-' , help = 'Input file path and name')
    args = parser.parse_args()
    main(args)
    