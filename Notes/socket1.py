import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket (endpoint)
mysock.connect(('data.pr4e.org', 80)) #Connect the socket to a domain name and a port
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode() #Get command in an UTF-8 string
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
