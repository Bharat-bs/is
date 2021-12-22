import socket, threading, random, math


def isprime(n):
    flag = False
    if n > 1:
        for i in range(2, int(n / 2)):
            if (n % i) == 0:
                flag = True
                break
    return not flag


def public_key():
    p = int(input("Enter a prime no : "))
    q = primitive_root(p - 1)
    return p, q


def primitive_root(p):
    r = 1
    l = []
    for i in range(2, p, 1):
        if math.gcd(i, p) == 1:
            l.append(i)
    return random.choice(l)


def keygenerated(priv, public):
    p, g = public
    return pow(g, priv, p)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8888))

priv = int(input("enter private key : "))
public = []
for i in range(2):
    msg = client.recv(4056).decode('ascii')
    client.send(b'sent')
    public.append(int(msg))

public = tuple(public)
print(public)

x = keygenerated(priv, public)

client.send(str(x).encode('ascii'))
y = int(client.recv(4056).decode('ascii'))

print("key ", pow(y, priv, public[0]))
