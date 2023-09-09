import customtkinter
from faker import Faker
from Table_1.ctk_tableview import CTkTableView


def table_1():
    root = customtkinter.CTk()
    root.title("CustomTkinter Table")
    root.geometry("450x400")

    headers = ["Name", "Age", "Email"]
    table = CTkTableView(root, headers)
    table.pack(expand=True, fill='both')

    data = []
    f = Faker()
    for n in range(100):
        name = f.name()
        age = f.random.randint(18, 70)
        email = f.email()
        data.append([name, age, email])

    table.update_table(data)

    root.mainloop()


if __name__ == "__main__":
    table_1()
