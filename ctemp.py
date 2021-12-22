import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.0.1',2222))

p=int(client.recv(2048).decode('ascii'))
print('')
g=int(client.recv(2048).decode('ascii'))
print('')
kA=int(client.recv(2048).decode('ascii'))
print('')
priv=3
y = pow(g,priv,p)
client.send(str(y).encode('ascii'))
print('')
key=pow(kA,priv,p)
print(key)