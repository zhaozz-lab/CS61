## local state
def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

wd = make_withdraw(20)
print(wd(5))
print(wd(10))


## built-in Iterator
def double_and_print(x):
    print('***', x, '=>', 2*x, '***')
    return 2*x
s = range(3, 7)
doubled = map(double_and_print, s)  # double_and_print not yet called
print("the type of doubled is {}".format(type(doubled)))
print(next(doubled))
print(next(doubled))

## filter------ filter the sequence that can't meet the commond
def is_odd(n):
    return n%2==1
x=range(1,10)
s = filter(is_odd,x)
print("the result of the filter is {} the value is {}".format(type(s),next(s)))
print("the result of the filter is {} the value is {}".format(type(s),next(s)))
print("the result of the filter is {} the value is {}".format(type(s),next(s)))


# zip
a = range(1,10)
b = range(11,20)
c = zip(a,b)
print("the resutl of zip is {}".format(c))
print(next(c))
print(next(c))

# generator
def letters_generator():
    current = 'a'
    while current <= 'd':
        yield current
        current = chr(ord(current)+1)
for letter in letters_generator():
    print(letter)













"""
OOP 
class create and special attribute
"""
def add_complex(z1,z2):
    return ComplexRI(z1.real + z2.real, z1.imag + z2.imag)


def mul_complex(z1,z2):
    return ComplexMA(z1.magnitude*z2.magnitude,z1.angle + z2.angle)

from math import atan2
class ComplexRI(object):
    """docstring for ComplexRI"""
    def __init__(self, real,imag):
        self.real = real
        self.imag = imag

    @property
    def magnitude(self):
        return (self.real**2+self.imag**2)**0.5
    
    @property
    def angle(self):
        return atan2(self.imag,self.real)

    def  __repr__(self):
        return "ComplexRI({0},{1})".format(self.real,self.imag) 



from math import sin, cos
class ComplexMA(object):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle
    
    @property
    def real(self):
        return self.magnitude * cos(self.angle)
    @property
    def imag(self):
        return self.magnitude * sin(self.angle)
    def __repr__(self):
        return 'ComplexMA({0}, {1})'.format(self.magnitude, self.angle)


from math import pi
print(add_complex(ComplexRI(1, 2), ComplexMA(2, pi/2)))
print(mul_complex(ComplexRI(0, 1), ComplexRI(0, 1)))


"""
generic function
"""
from fractions import gcd
class Rational(object):
    """doring for Rational"""
    def __init__(self,number,denom):
        g = gcd(number,denom)
        self.number = number
        self.denom = denom
    def __repr__(self):
        return 'Rational({0},{1})'.format(self.number,self.denom)

def add_rational(x,y):
    nx,dx = x.number,x.denom
    ny,dy = y.number,y.denom
    return Rational(nx*dy+ny*dx,dx*dy)

def mul_rational(x,y):
    return Rational(x.number*y.number,x.denom*y.denom)

    
"""
Type dispatching
"""
def iscomplex(z):
    return type(z) in (ComplexRI,ComplexMA)

def isrational(z):
    return type(z) == Rational

def add_complex_and_rational(z,r):
    return ComplexRI(z.real + r.number/r.denom,z.imag)

def add(z1,z2):
    """ add z1 and z2,which may be complex or rational."""
    if iscomplex(z1) and iscomplex(z2):
        return add_complex(z1,z2)
    elif iscomplex(z1) and isrational(z2):
        return add_complex_and_rational(z1,z2)
    elif isrational(z1) and iscomplex(z2):
        return add_complex_and_rational(z2,z1)
    else:
        return add_rational(z1,z2)


def type_tag(x):
    return type_tag_tags[type(x)]
type_tag_tags={ComplexRI:"com",ComplexMA:"com",Rational:"rat"}

def add(z1,z2):
    types = (type_tag(z1),type_tag(z2))
    return add.implementations[types](z1,z2)

add.implementations = {}
add.implementations[('com','com')] = add_complex
add.implementations[('com','rat')] = add_complex_and_rational
add.implementations[('rat','com')] = lambda x,y:add_complex_and_rational(y,x)
add.implementations[('rat','rat')] = add_rational

print(add(ComplexRI(1.5,0),Rational(3,2)))
print(add(Rational(5,3),Rational(1,2)))


"""
Data-directed programming
"""
def apply(operator_name,x,y):
    tags = (type_tag(x),type_tag(y))
    key = (operator_name,tags)
    return apply.implementations[key](x,y)

def mul_complex_and_rational(z,r):
    return ComplexMA(z.magnitude*r.number/r.denom,z.angle)

mul_rational_and_complex = lambda r,z:mul_complex_and_rational(z,r)
apply.implementations={('mul',('com','com')):mul_complex,
                      ('mul', ('com', 'rat')): mul_complex_and_rational,
                      ('mul', ('rat', 'com')): mul_rational_and_complex,
                      ('mul', ('rat', 'rat')): mul_rational
                       }
"""using the dictionary update method"""
adders = add.implementations.items()
apply.implementations.update({('add',tags):fn for (tags,fn) in adders})
apply('add', ComplexRI(1.5, 0), Rational(3, 2))
apply('mul', Rational(1, 2), ComplexMA(10, 1))


"""
Coercion
"""


"""
object abstraction
generic function:
1、shared interface 
2、type dispatching
3、type coercion
"""

"""
str:returns a human-readable string
repr: return a python expression
"""
from datetime import date
tues = date(2019,1,2)
print(str(tues))
print(repr(tues))
print(tues.__repr__())
print(tues.__str__())



