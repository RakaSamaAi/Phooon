import json
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox, simpledialog

class Contact:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.phone_number}"

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

        self.edit_button = tk.Button(self.root, text="Изменить контакт", command=self.edit_contact)
        self.edit_button.grid(row=2, column=0, pady=5)

        self.search_button = tk.Button(self.root, text="Поиск контакта", command=self.search_contact)
        self.search_button.grid(row=2, column=1, pady=5)

        self.display_button = tk.Button(self.root, text="Вывести список контактов", command=self.display_contacts)
        self.display_button.grid(row=3, column=0, pady=5)

        self.export_button = tk.Button(self.root, text="Экспорт в JSON", command=self.export_to_json)
        self.export_button.grid(row=3, column=1, pady=5)

        self.import_button = tk.Button(self.root, text="Импорт из JSON", command=self.import_from_json)
        self.import_button.grid(row=4, column=0, columnspan=2, pady=5)

    def add_contact(self):
        first_name = simpledialog.askstring("Добавление контакта", "Введите имя:")
        last_name = simpledialog.askstring("Добавление контакта", "Введите фамилию:")
        phone_number = simpledialog.askstring("Добавление контакта", "Введите номер телефона:")
        if first_name and last_name and phone_number:
            contact = Contact(first_name, last_name, phone_number)
            self.phone_book.add_contact(contact)
            messagebox.showinfo("Успешно", "Контакт добавлен")

    def delete_contact(self):
        first_name = simpledialog.askstring("Удаление контакта", "Введите имя контакта:")
        last_name = simpledialog.askstring("Удаление контакта", "Введите фамилию контакта:")
        if first_name and last_name:
            self.phone_book.delete_contact(first_name, last_name)
            messagebox.showinfo("Успешно", "Контакт удален")

    def edit_contact(self):
        first_name = simpledialog.askstring("Изменение контакта", "Введите имя контакта для изменения:")
        last_name = simpledialog.askstring("Изменение контакта", "Введите фамилию контакта для изменения:")
        if first_name and last_name:
            contact = self.phone_book.search_contact_by_name(first_name, last_name)
            if contact:
                new_first_name = simpledialog.askstring("Изменение контакта", "Введите новое имя:")
                new_last_name = simpledialog.askstring("Изменение контакта", "Введите новую фамилию:")
                new_phone_number = simpledialog.askstring("Изменение контакта", "Введите новый номер телефона:")
                if new_first_name and new_last_name and new_phone_number:
                    contact.first_name = new_first_name
                    contact.last_name = new_last_name
                    contact.phone_number = new_phone_number
                    messagebox.showinfo("Успешно", "Контакт успешно изменен")
            else:
                messagebox.showinfo("Ошибка", "Контакт не найден")

    def search_contact(self):
        keyword = simpledialog.askstring("Поиск контакта", "Введите ключевое слово для поиска:")
        if keyword:
            found_contacts = self.phone_book.search_contact(keyword)
            if found_contacts:
                messagebox.showinfo("Результаты поиска", "\n".join([str(contact) for contact in found_contacts]))
            else:
                messagebox.showinfo("Результаты поиска", "Контакт не найден")

    def display_contacts(self):
        contacts = self.phone_book.get_contacts()
        if contacts:
            messagebox.showinfo("Список контактов", "\n".join([str(contact) for contact in contacts]))
        else:
            messagebox.showinfo("Список контактов", "Контакты не найдены")

    def export_to_json(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if filename:
            with open(filename, 'w') as file:
                json.dump([vars(contact) for contact in self.phone_book.contacts], file)
            messagebox.showinfo("Экспорт", "Данные успешно экспортированы в JSON файл")

    def import_from_json(self):
        filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if filename:
            with open(filename, 'r') as file:
                data = json.load(file)
            self.phone_book.contacts = [Contact(**contact_data) for contact_data in data]
            messagebox.showinfo("Импорт", "Данные успешно импортированы из JSON файла")

class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, first_name, last_name):
        self.contacts = [c for c in self.contacts if c.first_name != first_name or c.last_name != last_name]

    def search_contact(self, keyword):
        return [c for c in self.contacts if keyword.lower() in c.first_name.lower() or keyword.lower() in c.last_name.lower()]

    def search_contact_by_name(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return contact
        return None

    def get_contacts(self):
        return self.contacts

if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneBookApp(root)
    root.mainloop()
