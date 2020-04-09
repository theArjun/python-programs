'''Print sum of the arguments using Positional Arguments.'''
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('num', type=int, nargs='+', help='List of one or more numbers')
args = parser.parse_args()
print(sum(args.num))
