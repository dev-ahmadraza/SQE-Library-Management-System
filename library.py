books = []
# Function to add books
def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "issued": False
    }

    books.append(book)

    print("Book added successfully!")

# Function to display all books
def view_books():
    if len(books) == 0:
        print("No books available")
    else:
        for book in books:
            print(book)

# Function to search book by ID
def search_book():
    search_id = input("Enter Book ID to search: ")

    for book in books:
        if book["id"] == search_id:
            print("Book Found:")
            print(book)
            return

    print("Book not found")


def issue_book():
    issue_id = input("Enter Book ID to issue: ")

    for book in books:
        if book["id"] == issue_id:

            if book["issued"]:
                print("Book already issued")

            else:
                book["issued"] = True
                print("Book issued successfully")

            return

    print("Book not found")


def return_book():
    return_id = input("Enter Book ID to return: ")

    for book in books:
        if book["id"] == return_id:

            if not book["issued"]:
                print("Book was not issued")

            else:
                book["issued"] = False
                print("Book returned successfully")

            return

    print("Book not found")