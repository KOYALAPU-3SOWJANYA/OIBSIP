import socket
import threading
PORT = 5050
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
def handle_client(conn, addr):
 print(f'[NEW CONNECTION] {addr} connected.')
 connected = True
 while connected:
   msg_lenght = conn.recv(HEADER).decode(FORMAT)
 if msg_lenght:
   msg_lenght = int(msg_lenght)
 msg = conn.recv(msg_lenght).decode(FORMAT)
 if msg == DISCONNECT_MESSAGE:
  connected = False
 print(f"[{addr}] {msg}")
 conn.close()
def start():
 server.listen()
 print(f'[LISTENING] server is listening on {SERVER}')
 while True:
  conn, addr = server.accept()
 thread = threading.Thread(target=handle_client, args=(conn, addr))
 thread.start()
 print(f'[ACTIVE CONNECTIONS]{threading.active_count()-1}')
print("[STARTING] server is starting......")
start()