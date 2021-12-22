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


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM )

host, port = '127.0.0.1', 7777
server.bind((host, port))
server.listen()
public = public_key()
priv=int(input("Enter private key : "))
print(public)
y=keygenerated(priv,public)
client, addr = server.accept()
for i in public:
    client.send(str(i).encode('ascii'))
    client.recv(4056)
x=int(client.recv(4056).decode('ascii'))
print(x)
client.send(str(y).encode('ascii'))
print("key ", pow(x, priv, public[0]))
