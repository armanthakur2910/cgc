

books = []
issued_books = {} 

def add_book():
    name = input("Enter book name: ").strip().title()
    if name in books or name in issued_books:
        print(f"{name} already exists in the library.")
    else:
        books.append(name)
        print(f"{name} is added successfully.")

def show_books():
    if not books:
        print("No books available.")
    else:
        print("Books available:")
        for b in books:
            print("-", b)

def issue_book():
    if not books:
        print("No books available to issue.")
        return
    show_books()
    name = input("Enter book name to issue: ").strip().title()
    if name in books:
        borrower = input("Enter borrower name: ").strip().title()
        issued_books[name] = borrower
        books.remove(name)
        print(f"{name} is issued to {borrower}.")
    else:
        print("Book not available.")

def return_book():
    if not issued_books:
        print("No books to return.")
        return
    print("Issued books:")
    for b, borrower in issued_books.items():
        print(f"- {b} (issued to {borrower})")
    name = input("Enter book name to return: ").strip().title()
    if name in issued_books:
        books.append(name)
        borrower = issued_books.pop(name)
        print(f"{name} returned successfully from {borrower}.")
    else:
        print("Book was never issued.")

def library():
    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("Thank you for using the library system!")
            break
        else:
            print("Invalid choice, please try again.")


library()