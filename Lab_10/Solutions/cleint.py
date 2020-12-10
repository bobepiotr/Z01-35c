import tkinter as tk
from tkinter import Entry, Label, Button, Frame, Canvas, Scrollbar
from tkinter import ttk
import requests as req

api = 'http://localhost:5000/'

default_font = ('Arial', 12)


class LoginWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Micro chat')

        self.client_name = ""

        self.login_frame = Frame(self.root)
        self.login_frame.grid(row=0)
        login_label = Label(self.login_frame, text='Enter your nickname', font=default_font)
        self.login_entry = Entry(self.login_frame, width=20, font=default_font)
        password_label = Label(self.login_frame, text='Enter your password', font=default_font)
        password_entry = Entry(self.login_frame, width=20, font=default_font)
        login_button = Button(self.login_frame, text='>>>', font=default_font,
                              command=lambda: self.login_button_on_click(password_entry.get()))

        login_label.grid(row=0)
        self.login_entry.grid(row=1)
        password_label.grid(row=2)
        password_entry.grid(row=3)
        login_button.grid(row=4)

    def start(self):
        self.root.mainloop()

    def login_button_on_click(self, password):
        self.client_name = self.login_entry.get()
        response = login_or_register(self.client_name, password).json()
        response_result = response['meta']['result']['result']

        if response_result == 'logged_in' or response_result == 'registered':
            self.create_chat_window()
        else:
            Label(self.login_frame, text='something went wrong', fg='red', font=default_font).grid(row=5)

    def create_chat_window(self):
        self.root.destroy()
        chat_window = ChatWindow(self.client_name)
        chat_window.start()


class ChatWindow:
    def __init__(self, client_name):
        self.client_name = client_name
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title(f'{self.client_name}\'s chat')

        self.chat_view = Label(self.root, height=10, width=40, bg='white', anchor='nw', font=default_font)

        chat_to_display = combine_messages_into_chat(self.client_name)
        if chat_to_display == '':
            chat_to_display = 'You have no messages :/'
        self.chat_view.configure(text=chat_to_display)  # setting text on chat label to client's chat
        self.chat_view.grid(row=1)

        Label(self.root, text="New message", font=default_font).grid(row=2)  # informational label
        message_field = Entry(self.root, background='white', font=default_font)
        message_field.grid(row=3)  # field for message content

        Label(self.root, text="Receiver", font=default_font).grid(row=4)  # informational label
        receiver_field = Entry(self.root, background='white', font=default_font)
        receiver_field.grid(row=5)  # field for receiver name

        send_button = Button(self.root, text='send', font=default_font,
                             command=lambda: self.send(receiver_field.get(), message_field.get()))
        send_button.grid(row=6)

        refresh_button = Button(self.root, text='refresh', font=default_font,
                                command=lambda: self.refresh())
        refresh_button.grid(row=7)

    def send(self, receiver_name, content):
        send_message(self.client_name, receiver_name, content)

    def refresh(self):
        msgs = combine_messages_into_chat(self.client_name)
        self.chat_view.configure(text=msgs)

    def start(self):
        self.root.mainloop()


def send_message(sender, receiver, msg_content):
    url = api + 'Users/send_message'
    data = {
        "meta": {
            "method": "send_message",
            "args": {
                "sender": sender,
                "receiver": receiver,
                "msg_content": msg_content
            }
        }
    }

    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    response = req.post(url, json=data, headers=headers)
    return response


def get_messages_addressed_to(username):
    url = api + 'Messages/get_messages_addressed_to'
    params = {"receiver_name": username}
    response = req.get(url, params=params)
    return response


def combine_messages_into_chat(username):
    messages_json = get_messages_addressed_to(username).json()
    dict_messages = messages_json['meta']['result']['result']  # {'id':[], 'rec':[], 'send':[], 'cont':[]}
    chat_string = ''
    for (s, c) in zip(dict_messages['sen'], dict_messages['cont']):
        chat_string += f'from: {s}: {c}\n'

    return chat_string


def login_or_register(username, password):
    url = api + 'Users/login_or_register_user'
    data = {
        "meta": {
            "method": "login_or_register_user",
            "args": {
                "user_name": username,
                "user_password": password
            }
        }
    }
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    response = req.post(url, json=data, headers=headers)
    print(response.json())
    return response


if __name__ == '__main__':
    login_window = LoginWindow()
    login_window.start()
