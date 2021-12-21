import math

alpha = "abcdefghijklmnopqrstuvwxyz"


def check_prime(n):
    flag = False
    for i in range(2, int(n/2)):
        if (n % i) == 0:
            flag = True
            break
    return not flag


def gcd(t):
    for e in range(2, t):
        if math.gcd(t, e) == 1:
            return e
    return -1


def encrypt(x, e, n):
    c = pow(x, e, n)
    return c


def eea(a, b):
    if (a % b == 0):
        return (b, 0, 1)
    else:
        gcd, s, t = eea(b, a % b)
        s = s - ((a // b) * t)
        return (gcd, t, s)


def multiplicative_inverse(e, r):
    gcd, s, _ = eea(e, r)
    if (gcd != 1):
        return gcd
    else:
        return s % r


def decrypt(c, e, n, t):
    d = multiplicative_inverse(e, t)
    return pow(c, d, n)


def encryption():
    p = int(input("Enter a prime number : "))
    if not check_prime(p):
        print("not a prime number ")
        exit(0)
    q = int(input("Enter a prime number : "))
    if not check_prime(q):
        print("not a prime number ")
        exit(0)
    n = p * q
    t = (p - 1) * (q - 1)
    msg = input("Enter the message to encrypt : ")
    e = gcd(t)
    cm = []
    print("n",n)
    print("t",t)
    print("e",e)

    for i in msg:
        x = alpha.index(i)
        cm.append(encrypt(x, e, n))
    return cm


def decryption():
    p = int(input("Enter a prime number : "))
    if not check_prime(p):
        print("not a prime number ")
        exit(0)
    q = int(input("Enter a prime number : "))
    if not check_prime(q):
        print("not a prime number ")
        exit(0)
    n = p * q
    t = (p - 1) * (q - 1)
    msg = input("Enter the message to decrypt : ")
    msg = msg.split(" ")
    e = gcd(t)
    pm = []
    pt = ""
    for i in msg:
        temp = decrypt(int(i), e, n, t)
        pm.append(temp)
        pt += alpha[temp]
    return pt


print(encryption())
print(decryption())
