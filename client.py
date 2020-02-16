import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 3000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

     # take input
    message = input(" -> ") 

    while message.lower().strip() != 'bye':
        print("Write w \n     Read r \n    q for quite  \n a for appending  \t")  # show in terminal
        message = input(" -> ") 
        client_socket.send(message.encode())  # send message
       # data = client_socket.recv(1024).decode()  # receive response
        #client_socket.send(s.encode())
        message = input(" -> ")  # again take input
        if(message== None):
            client_socket.close()

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()

