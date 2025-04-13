import socket

host = '127.0.0.1'
port = 5001

obj = socket.socket(socket.AF_INET)
obj.connect((host, port))
print ("Connected to server at: " + host + ":" + str(port))

while (message := input("type message (or 'q' to quit): ")) != 'q':
    obj.send(message.encode())
    print ("Waiting for message from server...")

    data = obj.recv(1024).decode()
    if not data:
        break
    print('Received from server: ' + data)
obj.close()