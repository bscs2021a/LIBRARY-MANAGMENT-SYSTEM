Group Members:
Name:Hajra  Roll. NO:BSCS_2021_34               Name:Saisha           Roll. NO:BSCS_2021_15     
 
 This system provides a userfriendly graphical interface for administrators to undertake various library administration activities. The
system's key features include the ability to add, remove, and amend member and book data, as well as the
ability to issue and track books issued to library members. Data is stored in CSV files indefinitely. Access to administrative functions is controlled by a login mechanism that
allows just the username "admin" and the password "123" to be used. To preserve data integrity, the system
enforces input validation, preventing the inclusion of duplicate members or books with the same details.
This manual provides a thorough description of the system's features, operations, and limitations, allowing
for effective library resource management.
Implementation:
Library Management System:
For frontend method, I used simple tkinter.

Functionalities:
- The program initializes the main application window using Tkinter.
- It sets up the color scheme and fonts for the user interface.
- The `logged_in` flag is used to track whether an administrator is logged in.
- An empty list `issued_books` is used to store issued books.
Login Dashboard
- The login dashboard is the initial interface presented to the user.
- The user can log in as an administrator by providing a username and password.
- The `login_as_admin` method verifies the provided credentials and grants access to the dashboard if they are correct.
Dashboard for Admin
- Upon successful login, the dashboard is created, providing access to member and book management features.
Member Management:
Member Data
- The system stores member data in the `members` list, where each member is represented by a list of three values:
Name, Roll Number, and Department.
Add Member
- The "Add Member" button opens a dialog for adding a new library member.
- The `save_member` method checks for valid input and ensures that a member with the same details is not added
twice.
- If the input is valid, the member is added, and data is saved to the "members.csv" file.
Remove Member
- The "Remove Member" button opens a dialog for removing an existing library member.
- The `perform_remove_member` method checks if the provided details match a member and removes them if found.
Display Members
- The "Display Members" button shows a list of all library members in the listbox.
  The `display_members` method populates the listbox with member information.
Book Management
Book Data
- The system stores book data in the `books` list, where each book is represented by a list of four values: Title, Author,
Genre, and Total Number of Books.
Add Book
- The "Add Book Record" button opens a dialog for adding a new book to the library.
- The `save_book` method checks for valid input and adds the book to the list.
Display Books
- The "Display Book Records" button shows a list of all library books in the listbox.
- The `display_books` method populates the listbox with book information.
Display Book Details
- The "Display Book" button shows the details of a selected book from the listbox.
Update Book
- The "Update Book Record" button opens a dialog for updating an existing book's details.
- The `perform_update_book` method allows changing the book's title, author, or the total number of available books.
Display Books by Author
- The "Books by Author" button allows the user to view books by a specific author.
Display Books by Genre
- The "Books by Genre" button allows the user to view books in a specific genre.
Issue Books
Issue Book
- The "Issue Book" button opens a dialog for issuing a book to a member.
- The `perform_issue_book` method validates member and book details, checks availability, updates the book count,
and records the issued book.
Display Issued Books
- The "Issued Books" button displays a list of books issued to members.
Data Persistence
- Member and book data are saved in CSV files ("members.csv" and "books.csv") to maintain data between sessions.
Restrictions
- Users must log in with the username "admin" and password "123" to access administrative features.
- Duplicate members or books with the same details cannot be added.
- Issuing a book checks for member existence, book availability, and updates the count.
- Input validation is enforced to ensure data consistency.

