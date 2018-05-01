import math
def ack(m,n):
    if m==0:
        return n+1
    elif  n==0:
        return ack(m-1,1)
    else:
        ackm=ack(m-1,ack(m,n-1))
        return ackm

print(ack(1,4))

def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]
def revmiddle (word):
    p= word [::-1]
    s= middle(p)
    return s


def is_palidrome(x):
    if first(x)==last(x):
        print("palidrome")
    if middle(x)==revmiddle(x):
        print("palidrome")
    else:
        print("not a palidrome")

print (is_palidrome("redivider"))

'''
a=input()
b=input()
def is_power (a,b):

    if a<b:
        return False

    elif a==b:
        return True

    else:
        return is_power(a/b,b)

print is_power(a,b)

'''


def gcd (a1,b1):
    if b1==0:
        return a1

    else:
        gcd(a1,a1%b1)

print gcd(0,1)




