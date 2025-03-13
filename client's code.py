import socket
import tkinter

server_name = 'localhost'
server_port = 30000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_name, server_port))


def display_text():
    text_to_send = text_entry.get()
    client_socket.send(text_to_send.encode())

    result = client_socket.recv(1024).decode()

    result_label.config(text=result)


root = tkinter.Tk()
root.title("dictionary")
root.geometry("1000x300")

text_entry = tkinter.Entry(root, width=40)
text_entry.pack(pady=30)

result_label = tkinter.Label(root, text="", width=150, height=4)
result_label.pack(pady=10)

display_button = tkinter.Button(root, text="search for its definition", command=display_text, width=50)
display_button.pack(pady=10)

root.mainloop()
