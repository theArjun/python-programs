# Let's overload + for str and integer.


class GCES:

    prefix = 'BE2017SE'

    def __add__(self, roll):
        return '{}0{}'.format(GCES.prefix, roll)

student_one = GCES()
print('Symbol no. is : ', student_one + 6)
