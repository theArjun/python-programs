# If a bird looks like a duck, swims like a duck, and quacks like a duck,
# then it probably is a duck.

# Similary, it any object has same method or attributes irrespective of their
# classes, it's okay to behave same.


class VSCode:

    def execute(self):

        print("Linting")
        print("Debuging")


class Sublime:

    def execute(self):

        print("Spell Check")
        print("Convention Check")
        print("Linting")
        print("Debuging")


class Editor:

    def code(self, editor):

        editor.execute()

# In this case, both VSCode and Sublime has execute method, so it doesn't
# matter if they are different, they can be passed to code () function
# of Editor classes, which runs execute () method.

# It is similar as implementing interfaces and the abstract methods in Java.

editor_ = VSCode()
e_one = Editor()
e_one.code(editor_)

editor_ = Sublime()
e_one.code(editor_)
