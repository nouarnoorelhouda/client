# coding: utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 1111))
while 1:
    print('server sent:', s.recv(1024).decode())
    s.send(b'Oi you sent something to me')

#print("Le nom du fichier que vous voulez récupérer:")
#file_name = input(">> ") # utilisez raw_input() pour les anciennes versions python
#s.send(file_name.encode())
#file_name = r"C:\Users\adminnennouar\PycharmProjects\VNFsTest\data\file%s" % (file_name,)
#r = s.recv(9999999)
#with open(file_name,'wb') as _file:
#    _file.write(r)
print(r)
