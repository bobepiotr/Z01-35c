import tkinter as tk
from tkinter import Entry, Label, Button, Frame
import chat_window as cw
import api_client as ac

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
        login_button = Button(self.login_frame, text='login', font=default_font,
                              command=lambda: self.login(password_entry.get()))

        register_button = Button(self.login_frame, text='register', font=default_font,
                                 command=lambda: self.register(password_entry.get()))

        self.error_label = Label(self.login_frame, font=default_font, fg='red')
        login_label.grid(row=0)
        self.login_entry.grid(row=1)
        password_label.grid(row=2)
        password_entry.grid(row=3)
        login_button.grid(row=4)
        register_button.grid(row=5)
        self.error_label.grid(row=6)

    def start(self):
        self.root.mainloop()

    def login(self, password):
        self.client_name = self.login_entry.get()
        if self.client_name == 'global':
            Label(self.login_frame, text='nickname not allowed', fg='red', font=default_font).grid(row=6)
            return

        response = ac.login(self.client_name, password).json()
        response_result = response['meta']['result']['result']

        if response_result == 'logged_in':
            user_id = response['meta']['result']['user_data']['id']
            self.create_chat_window(user_id)
            # self.error_label.configure(text='successfully logged')
        elif response_result == 'bad_credentials':
            self.error_label.configure(text='bad credentials')
        else:
            self.error_label.configure(text='something went wrong')

    def register(self, password):
        self.client_name = self.login_entry.get()
        if self.client_name == 'global':
            Label(self.login_frame, text='nickname not allowed', fg='red', font=default_font).grid(row=6)
            return

        response = ac.register(self.client_name, password).json()
        response_result = response['meta']['result']['result']

        if response_result == 'registered':
            user_id = response['meta']['result']['user_data']['id']
            self.create_chat_window(user_id)
            # self.error_label.configure(text='successfully registered')
        elif response_result == 'nickname_in_use':
            self.error_label.configure(text='nickname in use')
        else:
            self.error_label.configure(text='something went wrong')

    def create_chat_window(self, cli_id):
        self.root.destroy()
        chat_window = cw.ChatWindow(self.client_name, cli_id, '...')
        chat_window.start()


def create_sample_data():
    for i in range(8):
        ac.register("User"+str(i), "pass"+str(i))

    ac.send_message("User1", "User2", "Hello User2")
    ac.send_message("User2", "User1", "Hi User1, how are you?")
    ac.send_message("User1", "User2", "I'm fine, thanks. And you?")
    ac.send_message("User2", "User1", "Fine, thanks!")
    ac.send_message("User2", "User1", "Hello, thanks!")
    ac.send_message("User2", "User1", "That's cool!!!!!!!!!")
    ac.send_message("User2", "User1", "Bye!")
    ac.send_message("User1", "User2", "See you!")

    ac.send_message("User2", "User3", "u2 -> u3 mess1")
    ac.send_message("User3", "User2", "u3 -> u2 mess2")
    ac.send_message("User3", "User2", "u3 -> u2 mess3")
    ac.send_message("User2", "User3", "u2 -> u3 mess4")
    ac.send_message("User2", "User3", "u2 -> u3 mess5")

    for i in range(8):
        ac.send_message("User"+str(i), 'global', 'Hello global chat, my name is User '+str(i))


if __name__ == '__main__':
    # create_sample_data()
    w = LoginWindow()
    w.start()

