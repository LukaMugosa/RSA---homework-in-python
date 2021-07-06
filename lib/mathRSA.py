import random

def magnitude(number):
    res = 0
    while number > 0:
        res += 1
        number //= 10
    print("res = {} ".format(res))
    return res

def powerOfTwo(number, factors):
    if number == 0:
        return factors
    else:
        prev = 1
        test = 2

        while test <= number:
            prev = test
            test *= 2

        return powerOfTwo(number-prev, [prev] + factors)


def RSA(value, key):
    mod = key[0]
    exp = key[1]
    pot2 = powerOfTwo(exp, [])

    ind = 1
    res = 1
    currPot = value
    while ind <= pot2[len(pot2)-1]:

        if ind in pot2:
            res = (res*currPot)%mod
        ind *= 2

        currPot = (currPot*currPot)%mod
    return res


def miller_rabin(n, k):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in list(range(k)):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in list(range(r - 1)):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def prim_numfind(size,plus):
    n=pow(10,size-1)+plus
    if size==1:
        if plus==0:
            return 5
        else:
            return 7
    else:
        while n<pow( 10 , size ):
            x=pow(10,size-1)
            y=pow(10,size)
            n=random.randrange(x,y)
            if miller_rabin(n,40):
                return n
            n += 1
    return 0

def multiplicative_inverse(a, b):
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a
    ob = b
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob
    if ly < 0:
        ly += oa

    return lx


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

