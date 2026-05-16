import json

books = []


def load_books():

    global books

    try:
        with open("books.txt", "r") as file:
            content = file.read()

            if content:
                books = json.loads(content)

    except FileNotFoundError:
        books = []


def save_books():

    with open("books.txt", "w") as file:
        file.write(json.dumps(books))


def add_book():

    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    if not book_id or not title or not author:
        print("All fields are required")
        return

    for book in books:

        if book["id"] == book_id:
            print("Book ID already exists")
            return

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "issued": False
    }

    books.append(book)

    save_books()

    print("Book added successfully!")


def view_books():

    if len(books) == 0:
        print("No books available")

    else:

        print("\n===== Book List =====")

        for book in books:

            status = "Issued" if book["issued"] else "Available"

            print(
                f"ID: {book['id']}, "
                f"Title: {book['title']}, "
                f"Author: {book['author']}, "
                f"Status: {status}"
            )


def search_book():

    search_id = input("Enter Book ID to search: ")

    for book in books:

        if book["id"] == search_id:
            print("\nBook Found:")
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
                save_books()
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
                save_books()
                print("Book returned successfully")

            return

    print("Book not found")