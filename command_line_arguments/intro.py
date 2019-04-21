# System-specific parameters and functions. This module provides access to
# some variables used or maintained by the interpreter and to functions that
# interact strongly with the interpreter. It is always available. The list of
# command line arguments passed to a Python script.
import sys

# This imports the list and asssigns it to list
lst = sys.argv
# We can print the whole list through the loop or print particular element by
# indexing as well.
for i in lst:
    print(i)
# Printing the list elements by indexing
print(sys.argv[0])
