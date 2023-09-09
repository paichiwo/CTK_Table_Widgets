import customtkinter
from faker import Faker
from Table_2.ctk_tableview import CTkTableView


def fakeit(table):
    f = Faker()
    data = [[f.user_name(), f.password(), f.url()] for _ in range(100)]
    table.insert_rows(data)


def table_2():
    root = customtkinter.CTk()
    root.title("CustomTkinter Table")
    root.geometry("450x400")

    btn = customtkinter.CTkButton(root, text="Fake it", command=lambda: fakeit(table))
    btn.pack()

    values = [[f'test_user {n}', f'test_pass {n}', f'test_url {n}']for n in range(3)]

    table = CTkTableView(root, values=values)
    table.pack(expand=True, fill='both')

    root.mainloop()


if __name__ == "__main__":
    table_2()
