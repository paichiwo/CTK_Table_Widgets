import customtkinter
from faker import Faker
from ctktableview.my_tableview import CTkTableView


def fakeit():

    data = []
    f = Faker()
    for n in range(10):
        data.append([f.user_name(), f.password(), f.url()])
    print(data)
    table.insert_rows(data)


if __name__ == "__main__":
    root = customtkinter.CTk()
    root.title("CustomTkinter Table")
    root.geometry("450x400")

    btn = customtkinter.CTkButton(root, text="Fake it", command=fakeit)
    btn.pack()

    values = [
        ['test_user0', 'test_pass0', 'test_url0'],
        ['test_user1', 'test_pass1', 'test_url1']
    ]

    table = CTkTableView(root, values=values)
    table.pack(expand=True, fill='both')

    root.mainloop()

