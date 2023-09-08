import tkinter as tk
from customtkinter import CTkEntry
import customtkinter as ctk


class CTkTableView(ctk.CTkScrollableFrame):
    def __init__(self, master, headers, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.headers = headers
        self.data = []
        self.widths = [150, 50, 200]

        for col, header in enumerate(self.headers):
            label = tk.Label(self, text=header)
            label.grid(row=0, column=col, padx=5, pady=5)

        self.refresh_table()

    def add_row(self, row_number, row_data):
        if 0 <= row_number <= len(self.data):
            self.data.insert(row_number, row_data)
            self.refresh_table()

    def delete_row(self, row_number):
        if 0 <= row_number < len(self.data):
            del self.data[row_number]
            self.refresh_table()

    def get_table_data(self):
        table_data = []
        for row in range(1, len(self.data) + 1):
            row_data = []
            for col in range(len(self.headers)):
                entry = self.grid_slaves(row=row, column=col)[0]
                row_data.append(entry.get())
            table_data.append(row_data)
        return table_data

    def refresh_table(self):
        for widget in self.winfo_children():
            widget.grid_forget()

        for col, header in enumerate(self.headers):
            label = ctk.CTkLabel(self, text=header, font=("Any", 14, 'bold'))
            label.grid(row=0, column=col, padx=5, pady=5)

        for row, row_data in enumerate(self.data, start=1):
            for col, value in enumerate(row_data):
                entry = CTkEntry(self, width=self.widths[col])
                entry.insert(tk.END, value)
                entry.grid(row=row, column=col, padx=2, pady=2)

        submit_button = tk.Button(self, text="Submit", command=self.handle_submit)
        submit_button.grid(row=len(self.data) + 1, columnspan=len(self.headers), padx=10, pady=10)

    def update_table(self, new_data):
        # Clear the existing data
        self.data = []

        # Add the new data to the table
        for row in new_data:
            self.data.append(row)

        # Refresh the table with the new data
        self.refresh_table()

    def handle_submit(self):
        table_data = self.get_table_data()
        # Perform desired actions with the table data
        print(table_data)

