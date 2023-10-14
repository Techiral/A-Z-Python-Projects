import socket

serversocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host= socket.gethostname() #gets the IP Address of the host
port= 444

serversocket.bind((host, port))

serversocket.listen(3)

while True:
    clientsocket, address= serversocket.accept()
    
    print("recieved connection from" % str(address))

    message='hello! thankyou for connecting to the server'+"\r\n"
    clientsocket.send(message.encode())

    clientsocket.close()