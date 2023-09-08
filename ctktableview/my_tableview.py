
import customtkinter as ctk


class CTkTableView(ctk.CTkScrollableFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.frame = Frame(self, "username", "password", "website", fg_color='black')
        self.frame.pack(fill='both', ipady=10)

        self.master = master
        self.frame = Frame(self, "username", "password", "website", fg_color='black')
        self.frame.pack(fill='both', ipady=10, pady=10)

        self.master = master
        self.frame = Frame(self, "username", "password", "website", fg_color='black')
        self.frame.pack(fill='both', ipady=10)


class Frame(ctk.CTkFrame):
    def __init__(self, master, username, password, website, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master

        self.username = username
        self.password = password
        self.website = website

        self.username_label = None
        self.username_entry = None
        self.password_label = None
        self.password_entry = None
        self.website_label = None
        self.website_entry = None

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.gui()
        self.insert_data()

    def gui(self):

        self.username_label = ctk.CTkLabel(self, text="Username")
        self.username_label.grid(row=0, column=0, sticky='w', padx=20, pady=10)
        self.username_entry = ctk.CTkEntry(self)
        self.username_entry.grid(row=1, column=0, sticky='ew', padx=20)

        self.password_label = ctk.CTkLabel(self, text="Password")
        self.password_label.grid(row=2, column=0, sticky='w', padx=20, pady=10)
        self.password_entry = ctk.CTkEntry(self)
        self.password_entry.grid(row=3, column=0, sticky='ew', padx=20)

        self.website_label = ctk.CTkLabel(self, text="Website")
        self.website_label.grid(row=0, column=1, sticky='w', padx=20, pady=10)
        self.website_entry = ctk.CTkEntry(self)
        self.website_entry.grid(row=1, column=1, sticky='ew', padx=20)

    def insert_data(self):
        self.username_entry.insert(0, self.username)
        self.password_entry.insert(0, self.password)
        self.website_entry.insert(0, self.website)


