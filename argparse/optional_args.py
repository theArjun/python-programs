"""Demonstrate the Optional Arguments"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", "-v", help="Verbose Output", action="store_true")
parser.add_argument("--quiet", "-q", help="Short Output", action="store_true")
# Positional argument for a number input.
parser.add_argument("num", help="Arbitary Number Input")

args = parser.parse_args()

if args.verbose:
    print(f"The number you entered is {args.num}.")
elif args.quiet:
    print(args.num)
else:
    print(f"Input was {args.num}")
