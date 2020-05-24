""" Demonstrate Mutually exclusive arguments. """
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

group.add_argument("--verbose", "-v", help="Verbose Output", action="store_true")
group.add_argument("--quiet", "-q", help="Quiet Output", action="store_true")

parser.add_argument(
    "num", type=int, help="The list of one or more integer numbers.", nargs="+"
)
parser.add_argument(
    "--output", "-o", help="Output Result to a file.", action="store_true"
)

args = parser.parse_args()

sum_value = sum(args.num)
if args.verbose:
    message = f"The sum of the numbers is {sum_value}."
    print(message)
    if args.output:
        with open("output.txt", "w") as output:
            output.write(message)
            output.close()

elif args.quiet:
    message = sum_value
    print(message)
    if args.output:
        with open("output.txt", "w") as output:
            output.write(str(message))
            output.close()
