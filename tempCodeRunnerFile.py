import json
import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

class PhoneBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Телефонный справочник")

        self.phone_book = PhoneBook()

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Выберите действие:")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.add_button = tk.Button(self.root, text="Добавить контакт", command=self.add_contact)
        self.add_button.grid(row=1, column=0, pady=5)

        self.delete_button = tk.Button(self.root, text="Удалить контакт", command=self.delete_contact)
        self.delete_button.grid(row=1, column=1, pady=5)

        self.search_button = tk.Button(self.root, text="Поиск контакта", command=self.search_contact)
        self.search_button.grid(row=2, column=0, pady=5)

        self.display_button = tk.Button(self.root, text="Вывести список контактов", command=self.display_contacts)
        self.display_button.grid(row=2, column=1, pady=5)

    def add_contact(self):
        self.add_window = tk.Toplevel(self.root)
        self.add_window.title("Добавить контакт")

        self.first_name_label = tk.Label(self.add_window, text="Имя:")
        self.first_name_label.grid(row=0, column=0)

        self.first_name_entry = tk.Entry(self.add_window)
        self.first_name_entry.grid(row=0, column=1)

        self.last_name_label = tk.Label(self.add_window, text="Фамилия:")
        self.last_name_label.grid(row=1, column=0)

        self.last_name_entry = tk.Entry(self.add_window)
        self.last_name_entry.grid(row=1, column=1)

        self.phone_number_label = tk.Label(self.add_window, text="Телефон:")
        self.phone_number_label.grid(row=2, column=0)

        self.phone_number_entry = tk.Entry(self.add_window)
        self.phone_number_entry.grid(row=2, column=1)

        self.save_button = tk.Button(self.add_window, text="Сохранить", command=self.save_contact)
        self.save_button.grid(row=3, column=0, columnspan=2, pady=5)

    def save_contact(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        phone_number = self.phone_number_entry.get()
        self.phone_book.add_contact(Contact(first_name, last_name, phone_number))
        messagebox.showinfo("Успешно", "Контакт добавлен")
        self.add_window.destroy()

    def delete_contact(self):
        pass

    def search_contact(self):
        keyword = tk.simpledialog.askstring("Поиск контакта", "Введите ключевое слово для поиска:")
        if keyword:
            found_contacts = self.phone_book.search_contact(keyword)
            if found_contacts:
                messagebox.showinfo("Результаты поиска", "\n".join([f"{c.first_name} {c.last_name}: {c.phone_number}" for c in found_contacts]))
            else:
                messagebox.showinfo("Результаты поиска", "Контакт не найден")

    def display_contacts(self):
        contacts = self.phone_book.get_contacts()
        if contacts:
            messagebox.showinfo("Список контактов", "\n".join([f"{c.first_name} {c.last_name}: {c.phone_number}" for c in contacts]))
        else:
            messagebox.showinfo("Список контактов", "Контакты не найдены")

class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, first_name, last_name):
        self.contacts = [c for c in self.contacts if c.first_name != first_name or c.last_name != last_name]

    def search_contact(self, keyword):
        return [c for c in self.contacts if keyword.lower() in c.first_name.lower() or keyword.lower() in c.last_name.lower()]

    def get_contacts(self):
        return self.contacts

if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneBookApp(root)
    root.mainloop()