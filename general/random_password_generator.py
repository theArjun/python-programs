import string
import random
import pyperclip
import json


class RandomPasswordGenerator:

    def __init__(self):
        print("Welcome to Random Password Generator")
        self.limit = 0
        self.password = ''
        self.uppercase_choice = ''
        self.digit_choice = ''
        self.character_choice = ''

    def user_input(self):
        self.limit = int(input("\nEnter the length of the password in digits : "))

    def choice(self):
        self.uppercase_choice = input("Press Y for uppercase "
                                      "combination (else leave empty) : ").lower()
        self.digit_choice = input("Press Y for digit combination "
                                  "(else leave empty) : ").lower()
        self.character_choice = input("Press Y for special characters "
                                      "combination (else leave empty) : ").lower()

    def password_generator(self):

        self.user_input()
        self.choice()

        uppercase = string.ascii_uppercase if len(self.uppercase_choice) > 0 \
                                              and self.uppercase_choice[0] == 'y' else ''
        digit = string.digits if len(self.digit_choice) > 0 \
                                 and self.digit_choice[0] == 'y' else ''
        special_character = string.punctuation if len(self.character_choice) > 0\
                                                  and self.character_choice[0] == 'y' else ''

        self.password = ''.join(
            [random.choice(string.ascii_lowercase + uppercase + digit + special_character) for i in range(self.limit)])

    def show(self):
        print("Password : {}".format(self.password))

        print("\nPassword copied to Clipboard.")
        pyperclip.copy(self.password)


if __name__ == '__main__':

    r1 = RandomPasswordGenerator()
    r1.password_generator()
    r1.show()






