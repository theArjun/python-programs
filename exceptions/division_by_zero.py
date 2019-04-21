# Raises exception if a number is divided by zero.

try:
    num = 10
    print(num / 0)
except ZeroDivisionError:
    print("You tried division by zero.")
finally:
    print("But you're climbing the ladder of learning. Go on.")
