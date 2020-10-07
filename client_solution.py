from socket import *


sock = socket(AF_INET, SOCK_STREAM)
serverPort = 6789
server_address = (gethostname(), serverPort)
string = ""
f_name = input("Enter your file here: ")
m = "GET /" + f_name + " HTTP/1.1"
try:
    sock.connect(server_address)
    while True:
        try:
            sock.sendall(m.encode())

            data = sock.recv(16).decode()
            if data:
                print(str(data))

            while True:
                if data:
                    data = sock.recv(1024).decode()
                    string += str(data)
                else:
                    print("No more data to be received!")
                    break
            print(string)
        finally:
            print("File sent and output received.")
            break
except:
    print("Can't connect to the server.")
sock.close();