from socket import*
import threading

client_socket=socket(AF_INET, SOCK_STREAM)
name=input("Введіть ім'я")
client_socket.connect('localhost', 8080)
client_socket.send(name.encode())

def send_massage():
    while True:
        client_massage=input()
        if client_massage.lower()=='exit':
            client_socket.close()
            break
        client_socket.send(client_massage.encode())

while True:
    try:
        massage=client_socket.recv(1024).decode().strip()
        if massage:
            print(massage)
    except:
        break