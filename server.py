import socket
import threading
from _thread import *
from queue import *
def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 3000  # initiate port no above 1024
    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
    # configure how many client the server can listen simultaneously
    server_socket.listen(5)
    # List of sockets for select.select()
    sockets_list = [server_socket]
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = "You are no connected with client"
        data1="you can access my file"
        
        conn.send(data.encode())  # send data to the client
        conn.send(data1.encode())
        while True:
            try:
                s=conn.recv(1024).decode()
                if(s == 'w' or s =='W'):
                    f=open("komal.txt",'w')
                    sendd="Write in file::"
                    conn.send(sendd.encode())
                    data4=conn.recv(1024).decode()
                    f.write(data4)
                    f.close()
                elif(s=='r' or s=='R'):
                    f=open("komal.txt",'rb')
                    Buffer_size=4024
                    flow=f.read(Buffer_size)
                    conn.sendall(flow)
                

                elif(s=='q' or s=='Q'):
                   print("OK bye then")
                   conn.close()
                elif(s=='a' or s=='A'):
                    f=open("komal.txt",'a')
                    sendd1="append in file::"
                    conn.send(sendd1.encode())
                    data4=conn.recv(1024).decode()
                    f.write(data4)
                    f.close()
            
            except KeyboardInterrupt:
                 conn.close()
        

         # close the connection


if __name__ == '__main__':
    server_program()
