import socket
import sys
from pprint import pprint

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)

sock.bind(server_address)

sock.listen()

#need to respond to a GET request

while True:
    print ('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print ('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(2048)
            
            if data:

                print ("data")
                print(data.decode())
               
                #parse out the request and send back the GET response
                

                #here


                #connection.sendall(data)
            else:
                print ('no more data from', client_address)
                break
            
    finally:
        # Clean up the connection
        connection.close()