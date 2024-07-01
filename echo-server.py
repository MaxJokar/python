import socket

# server sets up a  listening socket
# HOST = "127.0.0.1" # local host 
HOST = "" 
PORT = 65432
# crete a socket object s
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    print(f"server binded to  :{PORT}")
    # s.listen()
    s.listen(3)
    print(f"socket is listening ")
    # conn : a new socket obj,  addr:internet address of client
    # conn, addr = s.accept() # a new port for c/s for interaction
# DATA EXCHANGE:
    # with conn:
        # print(f"Got connection from  {addr}")
    msg = ("thanks for connecting")
    while True:
        #     data = conn.recv()
        #     if not data:
        #         break
        #     conn.sendall(data)
        #     conn.send(msg.encode())
        #     conn.close()
        conn, addr = s.accept()
        print(f"Got connection from  {addr}")
        conn.send(msg.encode())
        conn.close()




# server binded to  :65432
# socket is listening 

# Got connection from  ('127.0.0.1', 63816)








