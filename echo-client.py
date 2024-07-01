import socket

# server sets up a  initiate  socket
HOST = "127.0.0.1" # local host 
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT)) # using the server host /port
    print(f"client binded to  :{PORT}")
    s.sendall(b"hello there ")
    data = s.recv(1024) # 1024 is  a buffer size
    print(data)
    s.close()





print(f"Recieved {data}")




# client binded to  :65432
# b'thanks for connecting'
# Recieved b'thanks for connecting'


