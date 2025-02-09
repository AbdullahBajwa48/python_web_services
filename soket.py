#The socket module allows python to create network connections
#Think of a socket as a communication end point, like a phone line between two computers.
import socket 

#socket.AF_INET refers to ip version_4 and socket.sock_stream refers to TCP to ensure reliable data transfer
#mysock acts like a phone to communicate to the server.
mysock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)


#Connect to the server with given link on port 80 which is standard port for http.
#Think this dialing a phone number to establish a connection.
mysock.connect(('data.pr4e.org',80))


#THis is an http request to retrieve a file.
#HTTP/1.0 is the version where as \r\n\r\n shows the end of the request.
# .encode() converts it into binary as socket send binary data.
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
mysock.close()



#Understand the Analogy 🧠

# A socket is like a phone call between two computers.
# connect() is like dialing the number.
# send() is like speaking into the phone.
# recv() is like listening to the response.
# close() is like hanging up the call.
