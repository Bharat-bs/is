import random
import socket, math, random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 2222))
server.listen(4)

p = 23


def primitive_root(g):
    l = []
    for i in range(2, p):
        if math.gcd(i, p) == 1:
            l.append(i)
    return random.choice(l)


g = 9

priv=4

x = pow(g,priv,p)

while (True):
    s, addr = server.accept()
    s.send(str(p).encode('ascii'))
    print('')
    s.send(str(g).encode('ascii'))
    print('')
    s.send(str(x).encode('ascii'))
    print('')
    kB = int(s.recv(4056).decode('ascii'))
    print('')
    key = pow(kB,priv,p)
    print(key)

