import socket

host = "127.0.0.1"
port = 5001

server = socket.socket(socket.AF_INET)

server.bind((host, port))
server.listen()
print("Server started at: " + host + ":" + str(port))
print("Waiting for connection...")

conn, addr = server.accept()
print("Connection from: " + str(addr))

while True:
   data = conn.recv(1024).decode()
   if not data:
      break
   data = str(data).upper()
   print ("Message from client: " + str(data))
   data = input("Type message (or 'q' to quit): ")
   if data.lower() == 'q':
       break
   conn.send(data.encode())
conn.close()