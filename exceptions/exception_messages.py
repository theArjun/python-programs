# Passes Message as attribute to Exceptions


class FamilyMemberError(Exception):
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return repr(self.data)


try:
    no_of_people = int(
        input("Enter number of people to be expected at family function : ")
    )
    if no_of_people < 10:
        raise FamilyMemberError("Too low no of family members for function.")
    if no_of_people > 5000:
        raise FamilyMemberError("Too many family members for a small family function.")
except FamilyMemberError as fme:
    print(fme.data)
else:
    print("Perfect no. for family function.")
finally:
    print("Celebrate well.")
