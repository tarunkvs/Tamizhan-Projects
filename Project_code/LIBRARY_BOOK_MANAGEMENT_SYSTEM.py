import datetime
import json
My_FILE = "librarydata.json"
try:
    with open(My_FILE, "r") as f:
        library = json.load(f)
except FileNotFoundError:
    library = {"books": {}, "issued": {}}
def save_data():
    with open(My_FILE, "w") as f:
        json.dump(library, f, indent=4)
def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    if book_id in library["books"]:
        print("Book ID already exists!")
    else:
        library["books"][book_id] = {"title": title, "author": author}
        print("Book added successfully!")
        save_data()
def remove_book():
    book_id = input("Enter book ID to remove: ")
    if book_id in library["books"]:
        del library["books"][book_id]
        print("Book removed!")
        save_data()
    else:
        print("Book ID not found.")
def issue_book():
    book_id = input("Enter book ID to issue: ")
    student = input("Enter student name: ")
    if book_id in library["books"] and book_id not in library["issued"]:
        issue_date = datetime.date.today()
        due_date = issue_date + datetime.timedelta(days=7)
        library["issued"][book_id] = {"student": student, "issue_date": str(issue_date), "due_date": str(due_date)}
        print(f"Book issued to {student} until {due_date}")
        save_data()
    else:
        print("Book not available or already issued.")
def return_book():
    book_id = input("Enter book ID to return: ")
    if book_id in library["issued"]:
        issue_data = library["issued"][book_id]
        due_date = datetime.datetime.strptime(issue_data["due_date"], "%Y-%m-%d").date()
        today = datetime.date.today()
        days_late = (today - due_date).days
        fine = 0
        if days_late > 0:
            fine = days_late * 2
        print(f"Book returned. Fine: ₹{fine}")
        del library["issued"][book_id]
        save_data()
    else:
        print("Book was not issued.")
def view_books():
    if not library["books"]:
        print("No books available.")
    else:
        print("\nAvailable Books:")
        for book_id, info in library["books"].items():
            status = "Issued" if book_id in library["issued"] else "Available"
            print(f"{book_id}: {info['title']} by {info['author']} ({status})")
def main():
    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View Books")
        print("6. Exit")
        mychoice = input("Enter your choice (1-6): ")
        if mychoice == '1':
            add_book()
        elif mychoice == '2':
            remove_book()
        elif mychoice == '3':
            issue_book()
        elif mychoice == '4':
            return_book()
        elif mychoice == '5':
            view_books()
        elif mychoice == '6':
            print("Exiting Library System.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
