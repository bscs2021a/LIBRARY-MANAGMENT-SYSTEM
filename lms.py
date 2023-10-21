import tkinter as tk
from tkinter import simpledialog, messagebox
import csv

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.logged_in = False
        self.issued_books = []

        # Customize the colors and fonts
        self.bg_color = "#f0f0f0"
        self.text_color = "#333333"
        self.button_color = "#4caf50"
        self.font = ("Helvetica", 14)

        # Create login dashboard
        self.create_login_dashboard()

    def create_login_dashboard(self):
        self.login_frame = tk.Frame(self.root, bg=self.bg_color)
        self.login_frame.pack()

        tk.Label(self.login_frame, text="Library Management System", font=("Helvetica", 18, "bold"), bg=self.bg_color, fg=self.text_color).pack(pady=10)

        self.admin_frame = tk.Frame(self.login_frame, bg=self.bg_color)
        self.admin_frame.pack(pady=10)

        tk.Label(self.admin_frame, text="Admin Login", font=self.font, bg=self.bg_color, fg=self.text_color).pack()

        self.admin_username_label = tk.Label(self.admin_frame, text="Username:", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.admin_username_label.pack(side="left")
        self.admin_username_entry = tk.Entry(self.admin_frame, font=self.font)
        self.admin_username_entry.pack(side="left")

        self.admin_password_label = tk.Label(self.admin_frame, text="Password:", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.admin_password_label.pack(side="left")
        self.admin_password_entry = tk.Entry(self.admin_frame, show="*", font=self.font)
        self.admin_password_entry.pack(side="left")

        self.login_as_admin_button = tk.Button(self.login_frame, text="Login as Admin", command=self.login_as_admin, bg=self.button_color, fg="white", font=self.font)
        self.login_as_admin_button.pack(pady=10)

        self.student_frame = tk.Frame(self.login_frame, bg=self.bg_color)
        self.student_frame.pack(pady=10)

    def login_as_admin(self):
        username = self.admin_username_entry.get()
        password = self.admin_password_entry.get()
        if username == "admin" and password == "123":
            self.logged_in = True
            self.login_frame.pack_forget()  # Hide the login dashboard
            self.create_dashboard()
        else:
            messagebox.showinfo("Login Failed", "Invalid admin credentials.")

    def create_dashboard(self):
        # Implement the dashboard for both admin and student logins
        self.members = []
        self.books = []
        self.load_data()

        self.create_member_management()
        self.create_book_management()

    def save_data(self):
        with open("members.csv", "w", newline="") as members_file:
            writer = csv.writer(members_file)
            writer.writerows(self.members)

        with open("books.csv", "w", newline="") as books_file:
            writer = csv.writer(books_file)
            writer.writerows(self.books)

    def load_data(self):
        try:
            with open("members.csv", "r") as members_file:
                reader = csv.reader(members_file)
                self.members = list(reader)

            with open("books.csv", "r") as books_file:
                reader = csv.reader(books_file)
                self.books = list(reader)
        except FileNotFoundError:
            pass

    def create_member_management(self):
        # Member Management GUI
        self.member_frame = tk.Frame(self.root)
        self.member_frame.pack()

        tk.Label(self.member_frame, text="Library Members").pack(pady=10)

        self.member_listbox = tk.Listbox(self.member_frame, width=70, height=10)
        self.member_listbox.pack(pady=10)

        self.add_member_button = tk.Button(
            self.member_frame, text="Add Member", command=self.add_member)
        self.add_member_button.pack(side="left", padx=10)

        self.remove_member_button = tk.Button(
            self.member_frame, text="Remove Member", command=self.remove_member
        )
        self.remove_member_button.pack(side="left", padx=10)

        self.display_members_button = tk.Button(
            self.member_frame, text="Display Members", command=self.display_members
        )
        self.display_members_button.pack(side="left", padx=10)

    def create_book_management(self):
        # Book Management GUI
        self.book_frame = tk.Frame(self.root)
        self.book_frame.pack()

        tk.Label(self.book_frame, text="Library Books").pack(pady=10)

        self.book_listbox = tk.Listbox(self.book_frame, width=70, height=10)
        self.book_listbox.pack(pady=10)

        self.add_book_button = tk.Button(
            self.book_frame, text="Add Book Record", command=self.add_book
        )
        self.add_book_button.pack(side="left", padx=3)

        self.display_books_button = tk.Button(
            self.book_frame, text="Display Book Records", command=self.display_books
        )
        self.display_books_button.pack(side="left", padx=3)

        self.display_book_button = tk.Button(
            self.book_frame, text="Display Book", command=self.display_book
        )
        self.display_book_button.pack(side="left", padx=3)

        self.update_book_button = tk.Button(
            self.book_frame, text="Update Book Record", command=self.update_book
        )
        self.update_book_button.pack(side="left", padx=3)

        self.books_by_author_button = tk.Button(
            self.book_frame, text="Books by Author",command=self.display_books_by_author
        )
        self.books_by_author_button.pack(side="left", padx=3)

        self.books_by_genre_button = tk.Button(
            self.book_frame, text="Books by Genre", command=self.display_books_by_genre
        )
        self.books_by_genre_button.pack(side="left", padx=2)

        self.issue_book_button = tk.Button(
            self.book_frame, text="Issue Book", command=self.issue_book
        )
        self.issue_book_button.pack(side="left", padx=2)

        self.issued_books_button = tk.Button(
            self.book_frame, text="Issued Books", command=self.display_issued_books
        )
        self.issued_books_button.pack(side="left", padx=2)

    def add_member(self):
        member_dialog = tk.Toplevel(self.root)
        member_dialog.title("Add Member")

        tk.Label(member_dialog, text="Enter Member Details:").pack()

        name_label = tk.Label(member_dialog, text="Name:")
        name_label.pack()
        name_entry = tk.Entry(member_dialog)
        name_entry.pack()

        roll_number_label = tk.Label(member_dialog, text="Roll Number:")
        roll_number_label.pack()
        roll_number_entry = tk.Entry(member_dialog)
        roll_number_entry.pack()

        department_label = tk.Label(member_dialog, text="Department:")
        department_label.pack()
        department_entry = tk.Entry(member_dialog)
        department_entry.pack()

        add_button = tk.Button(member_dialog, text="Add Member", command=lambda: self.save_member(name_entry.get(), roll_number_entry.get(), department_entry.get(), member_dialog))
        add_button.pack()

    def save_member(self, name, roll_number, department, dialog):
        if name and roll_number and department:
            for member in self.members:
                if len(member) >= 3 and member[0] == name and member[1] == roll_number and member[2] == department:
                    messagebox.showinfo("Member Already Exists", "This member is already added.")
                    dialog.destroy()
                    return
            self.members.append([name, roll_number, department])
            self.save_data()
            self.display_members()
            dialog.destroy()
        else:
            messagebox.showinfo("Invalid Input", "Please provide all member information.")

    def remove_member(self):
        member_dialog = tk.Toplevel(self.root)
        member_dialog.title("Remove Member")

        tk.Label(member_dialog, text="Enter Member Details to Remove:").pack()

        name_label = tk.Label(member_dialog, text="Name:")
        name_label.pack()
        name_entry = tk.Entry(member_dialog)
        name_entry.pack()

        roll_number_label = tk.Label(member_dialog, text="Roll Number:")
        roll_number_label.pack()
        roll_number_entry = tk.Entry(member_dialog)
        roll_number_entry.pack()

        department_label = tk.Label(member_dialog, text="Department:")
        department_label.pack()
        department_entry = tk.Entry(member_dialog)
        department_entry.pack()

        remove_button = tk.Button(member_dialog, text="Remove Member", command=lambda: self.perform_remove_member(name_entry.get(), roll_number_entry.get(), department_entry.get(), member_dialog))
        remove_button.pack()

    def perform_remove_member(self, name, roll_number, department, dialog):
        if name and roll_number and department:
            for member in self.members:
                if len(member) >= 3 and member[0] == name and member[1] == roll_number and member[2] == department:
                    self.members.remove(member)
                    self.save_data()
                    self.display_members()
                    dialog.destroy()
                    return
            messagebox.showinfo("Remove Member", f"No member found with the provided details.")
        else:
            messagebox.showinfo("Invalid Input", "Please provide all member information.")

    def display_members(self):
        self.member_listbox.delete(0, tk.END)
        for member in self.members:
            if len(member) >= 3:
                self.member_listbox.insert(tk.END, f"Name: {member[0]}, Roll Number: {member[1]}, Department: {member[2]}")

    def add_book(self):
        book_dialog = tk.Toplevel(self.root)
        book_dialog.title("Add Book")

        tk.Label(book_dialog, text="Enter Book Details:").pack()

        title_label = tk.Label(book_dialog, text="Title:")
        title_label.pack()
        title_entry = tk.Entry(book_dialog)
        title_entry.pack()

        author_label = tk.Label(book_dialog, text="Author:")
        author_label.pack()
        author_entry = tk.Entry(book_dialog)
        author_entry.pack()

        genre_label = tk.Label(book_dialog, text="Genre:")
        genre_label.pack()
        genre_entry = tk.Entry(book_dialog)
        genre_entry.pack()

        total_books_label = tk.Label(book_dialog, text="Total Number of Books:")
        total_books_label.pack()
        total_books_entry = tk.Entry(book_dialog)
        total_books_entry.pack()

        add_button = tk.Button(book_dialog, text="Add Book", command=lambda: self.save_book(title_entry.get(), author_entry.get(), genre_entry.get(), total_books_entry.get(), book_dialog))
        add_button.pack()

    def save_book(self, title, author, genre, total_books, dialog):
        if title and author and genre and total_books:
            try:
                total_books = int(total_books)
                self.books.append([title, author, genre, total_books])
                self.save_data()
                self.display_books()
                dialog.destroy()
            except ValueError:
                messagebox.showinfo("Invalid Input", "Please enter a valid number for 'Total Number of Books'.")
        else:
            messagebox.showinfo("Invalid Input", "Please provide all book information.")

    def remove_book(self):
        book_dialog = tk.Toplevel(self.root)
        book_dialog.title("Remove Book")

        tk.Label(book_dialog, text="Enter Book Details to Remove:").pack()

        title_label = tk.Label(book_dialog, text="Title:")
        title_label.pack()
        title_entry = tk.Entry(book_dialog)
        title_entry.pack()

        author_label = tk.Label(book_dialog, text="Author:")
        author_label.pack()
        author_entry = tk.Entry(book_dialog)
        author_entry.pack()

        remove_button = tk.Button(book_dialog, text="Remove Book", command=lambda: self.perform_remove_book(title_entry.get(), author_entry.get(), book_dialog))
        remove_button.pack()

    def perform_remove_book(self, title, author, dialog):
        if title and author:
            for book in self.books:
                if len(book) >= 4 and book[0] == title and book[1] == author:
                    self.books.remove(book)
                    self.save_data()
                    self.display_books()
                    dialog.destroy()
                    return
            messagebox.showinfo("Remove Book", "Book not found with the provided details.")
        else:
            messagebox.showinfo("Invalid Input", "Please provide book title and author.")

    def display_books(self):
        self.book_listbox.delete(0, tk.END)
        for book in self.books:
            if len(book) >= 4:
                self.book_listbox.insert(tk.END, f"Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}, Total Books: {book[3]}")

    def display_book(self):
        selected_index = self.book_listbox.curselection()

        if selected_index:
            selected_book = self.books[int(selected_index[0])]

            if len(selected_book) >= 4:
                title, author, genre, total_books = selected_book
                messagebox.showinfo("Book Details", f"Title: {title}\nAuthor: {author}\nGenre: {genre}\nTotal Books: {total_books}")
            else:
                messagebox.showinfo("Book Details", "Invalid book data.")

    def update_book(self):
        book_dialog = tk.Toplevel(self.root)
        book_dialog.title("Update Book")

        tk.Label(book_dialog, text="Enter Book Details to Update:").pack()

        title_label = tk.Label(book_dialog, text="Title:")
        title_label.pack()
        title_entry = tk.Entry(book_dialog)
        title_entry.pack()

        author_label = tk.Label(book_dialog, text="Author:")
        author_label.pack()
        author_entry = tk.Entry(book_dialog)
        author_entry.pack()

        new_title_label = tk.Label(book_dialog, text="New Title:")
        new_title_label.pack()
        new_title_entry = tk.Entry(book_dialog)
        new_title_entry.pack()

        new_author_label = tk.Label(book_dialog, text="New Author:")
        new_author_label.pack()
        new_author_entry = tk.Entry(book_dialog)
        new_author_entry.pack()

        new_total_books_label = tk.Label(book_dialog, text="New Total Number of Books:")
        new_total_books_label.pack()
        new_total_books_entry = tk.Entry(book_dialog)
        new_total_books_entry.pack()

        update_button = tk.Button(book_dialog, text="Update Book", command=lambda: self.perform_update_book(title_entry.get(), author_entry.get(), new_title_entry.get(), new_author_entry.get(), new_total_books_entry.get(), book_dialog))
        update_button.pack()

    def perform_update_book(self, title, author, new_title, new_author, new_total_books, dialog):
        if title and author and new_title and new_author:
            for book in self.books:
                if len(book) >= 4 and book[0] == title and book[1] == author:
                    book[0] = new_title
                    book[1] = new_author
                    if new_total_books:
                        try:
                            new_total_books = int(new_total_books)
                            book[3] = new_total_books
                        except ValueError:
                            messagebox.showinfo("Invalid Input", "Please enter a valid number for 'New Total Number of Books'.")
                            return

                    self.save_data()
                    self.display_books()
                    dialog.destroy()
                    return
            messagebox.showinfo("Update Book", "Book not found with the provided details.")
        else:
            messagebox.showinfo("Invalid Input", "Please provide all book information.")

    def display_books_by_author(self):
        author_name = simpledialog.askstring("Books by Author", "Enter Author Name:")
        if author_name:
            matching_books = [book for book in self.books if book[1].lower() == author_name.lower()]
            if matching_books:
                book_list = "\n".join([f"Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}, Total Books: {book[3]}" for book in matching_books])
                messagebox.showinfo("Books by Author", f"Books by {author_name}:\n{book_list}")
            else:
                messagebox.showinfo("Books by Author", f"No books found for author: {author_name}")

    def display_books_by_genre(self):
        genre = simpledialog.askstring("Books by Genre", "Enter Genre:")
        if genre:
            matching_books = [book for book in self.books if book[2].lower() == genre.lower()]
            if matching_books:
                book_list = "\n".join([f"Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}, Total Books: {book[3]}" for book in matching_books])
                messagebox.showinfo("Books by Genre", f"Books in Genre {genre}:\n{book_list}")
            else:
                messagebox.showinfo("Books by Genre", f"No books found in the genre: {genre}")

    def issue_book(self):
        issue_dialog = tk.Toplevel(self.root)
        issue_dialog.title("Issue Book")

        # Create labels and entry fields for member details
        tk.Label(issue_dialog, text="Member Details:").pack()
        member_name_label = tk.Label(issue_dialog, text="Member Name:")
        member_name_label.pack()
        member_name_entry = tk.Entry(issue_dialog)
        member_name_entry.pack()

        roll_number_label = tk.Label(issue_dialog, text="Roll Number:")
        roll_number_label.pack()
        roll_number_entry = tk.Entry(issue_dialog)
        roll_number_entry.pack()

        department_label = tk.Label(issue_dialog, text="Department:")
        department_label.pack()
        department_entry = tk.Entry(issue_dialog)
        department_entry.pack()

        # Create labels and entry fields for book details
        tk.Label(issue_dialog, text="Book Details:").pack()
        book_title_label = tk.Label(issue_dialog, text="Book Title:")
        book_title_label.pack()
        book_title_entry = tk.Entry(issue_dialog)
        book_title_entry.pack()

        author_name_label = tk.Label(issue_dialog, text="Author Name:")
        author_name_label.pack()
        author_name_entry = tk.Entry(issue_dialog)
        author_name_entry.pack()

        issue_button = tk.Button(issue_dialog, text="Issue Book", command=lambda: self.perform_issue_book(member_name_entry.get(), roll_number_entry.get(), department_entry.get(), book_title_entry.get(), author_name_entry.get(), issue_dialog))
        issue_button.pack()

    def perform_issue_book(self, member_name, roll_number, department, book_title, author_name, dialog):
        if member_name and roll_number and department and book_title and author_name:
            for member in self.members:
                if len(member) >= 3 and member[0] == member_name and member[1] == roll_number and member[2] == department:
                    for book in self.books:
                        if len(book) >= 4 and book[0] == book_title and book[1] == author_name and int(book[3]) > 0:
                            book[3] = str(int(book[3]) - 1)  # Decrement the total number of available books

                            # Create a record of the issued book
                            issued_book = [book_title, author_name, member_name]
                            self.issued_books.append(issued_book)

                            self.save_data()
                            self.display_books()
                            messagebox.showinfo("Issue Book", f"Successfully issued to {member_name}")
                            dialog.destroy()
                            return
                    messagebox.showinfo("Issue Book", "Book not found or no available copies.")
                    return
            messagebox.showinfo("Issue Book", "Member not found with the provided details.")
        else:
            messagebox.showinfo("Invalid Input", "Please provide all member and book information.")


    def display_issued_books(self):
        if self.issued_books:
            book_list = "\n".join([f"Title: {book[0]}, Author: {book[1]}, Member: {book[2]}" for book in self.issued_books])
            messagebox.showinfo("Issued Books", f"Issued Books:\n{book_list}")
        else:
            messagebox.showinfo("Issued Books", "No books have been issued.")


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.configure(bg="#f0f0f0")  # Set a consistent background color
    root.geometry("800x600")  # Set the initial window size
    root.mainloop()
