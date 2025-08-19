from timeit import Timer
Timer ('t=a; a=b; b=t', 'a=1; b=2').timeit()

#!/usr/bin/python3

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i =imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)