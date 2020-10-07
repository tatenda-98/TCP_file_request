# TCP_file_request
#Python Code that uses a tcp connection to connect a client to a server and display contents of a file from retrieved from the client
Create a TCP server socket 
Assign a port number 
Bind the socket to a server address and server port 
While the server is listening, set up a new connection from the client 
Receive a request message from the client 
Client inputs the file that is to be read 
Extract the path of the requested object of the message 
Store the content of the file in a temporary buffer
Send the HTTP response header line to the connection socket 
Send the content of the requested file to the connection socket 
The client receives the file contents and it's displayed 
Close the connection on both ends 
