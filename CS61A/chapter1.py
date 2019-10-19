# fucnction as argument
def sum_naturals(n):
	total,k = 0,1
	while k<=n:
		total,k = total+k,k+1
	return total


def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k*k*k, k + 1
    return total


def pi_sum(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / ((4*k-3) * (4*k-1)), k + 1
    return total


def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def cube(x):
    return x*x*x


def pi_term(x):
    return 8 / ((4*x-3) * (4*x-1))
print(summation(3,cube))


# function as general method
# iteration judge x^2 equal to x+1
def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess


def golden_update(guess):
    return 1/guess + 1

def approx_eq(x, y, tolerance=1e-15):
        return abs(x - y) < tolerance

def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)

improve(golden_update, square_close_to_successor)

# Defining Functions: Nested Definitions
# Example Newton's method,牛顿方法的实现原理为，取初始点切线的根作为下一次的预测点，直到函数的值接近0为止
def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update


def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

# define f(x) as x^2 - a,the derivation is 2x
def square_root_newton(a):
    def f(x):
        return x * x - a
    def df(x):
        return 2 * x
    return find_zero(f, df)

print(square_root_newton(64))


def power(x, n):
    """Return x * x * x * ... * x for x repeated n times."""
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product

def nth_root_of_a(n, a):
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n-1)
    return find_zero(f, df)

print(nth_root_of_a(2,64))
print(nth_root_of_a(3,64))
print(nth_root_of_a(6,64))


## Currying
# first call h,then y
def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h
print(curried_pow(2)(3))

def map_to_range(start, end, f):
        while start < end:
            print(f(start))
            start = start + 1
print(map_to_range(0,2,curried_pow(2)))


## Lambda  Expressions
s=lambda x:x*x
print(s(2))


"""
python decorater 
"""
def trace1(fn):
    def  wrapped(x):
        print('->',fn,'(',x,')')
        return fn(x)
    return wrapped

@trace1
def triple(x):
    return x*3

print(triple(12))

