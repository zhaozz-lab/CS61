# coding:utf-8


def pig_latin(w):
    if starts_with_a_vowel(w):
        return w + 'ay'
    return pig_latin(w[1:] + w[0])

 # def starts_with_a_vowel():
 #  pass
def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-2)+fib(n-1)
print(fib(6)) 

def memo(f):
    cache = {}
    def memorized(n):
        if n not in cache:
            cache[n]= f(n)
        return cache[n]
    return memorized
fib = memo(fib)
print(fib(40))