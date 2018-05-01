
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
recurse(3, 0)

def fibon(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return fibon(a-1)+fibon(a-2)
print (fibon(3))


def ackerman (m,n):
    if m==0:
       return n+1
    elif n==0:
        return ackerman(m-1,1)
    return ackerman(m - 1, ackerman(m, n - 1))

ackerman(3,4)

def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]
def revmiddle (word):
    return middle(word) [::-1]

def ispal(a):
    if revmiddle(a)==middle(a):
        return ("palidrome")
    else:
        return ("not a palidrome")

print (ispal("hellor"))


def is_power (a,b):
    if a<b:
        return False
    elif a==b:
        return True
    else:
        if a%b==0:
         return is_power(a/b,b)
print (is_power(8,2))


def is_gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    else:
        n = a / b

        return is_gcd(b,n)

print (is_gcd(15,5))


def countdown(n):
    while n > 0:
        print(n)
        n=n-1
print('Blastoff!')


countdown(10)


def prod9(n):
    x=n-1
    y=10-n
    x=str(x)
    y=str(y)
    print(x+y)
prod9(5)

import math

print (eval("1+2+1"))

def eval_loop (x):
    while x!="done":

        x = input()
        eval(x)
        print (x)
print (eval_loop("1+2+1"))
