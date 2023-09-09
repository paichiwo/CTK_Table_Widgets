import customtkinter as ctk
from Table_1.main import table_1
from Table_2.main import table_2

root = ctk.CTk()
root.title("customtkinter tableview")

btn_1 = ctk.CTkButton(root, text="Table_1", command=table_1)
btn_2 = ctk.CTkButton(root, text="Table_2", command=table_2)

btn_1.grid(row=0, column=0, padx=40, pady=20)
btn_2.grid(row=0, column=1, padx=40, pady=20)

root.mainloop()
