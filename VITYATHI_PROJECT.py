class Book:
    """Represents a single book in the library."""
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False  
    # Track if the book is currently checked out

    def __str__(self):
        """String representation for printing book details."""
        status = "Checked Out" if self.is_checked_out else "Available"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}"

class Library:
    """Manages the collection of books."""
    def __init__(self):
        # A list to store all Book objects
        self.books = []

    def add_book(self, book):
        """Adds a new book to the library collection."""
        if isinstance(book, Book):
            self.books.append(book)
            print(f"\n Book '{book.title}' added successfully.")
        else:
            print("\n Error: Only Book objects can be added.")

    def list_books(self):
        """Prints details of all books in the library."""
        if not self.books:
            print("\n The library currently has no books.")
            return

        print("\n--- Current Library Collection ---")
        for i, book in enumerate(self.books, 1):
            print(f"[{i}] {book}")
        print("----------------------------------")

    def search_book(self, title):
        """Searches for a book by its title (case-insensitive, partial match)."""
        found_books = []
        search_title = title.lower()

        for book in self.books:
            if search_title in book.title.lower():
                found_books.append(book)

        if found_books:
            print(f"\n--- Found {len(found_books)} Book(s) ---")
            for book in found_books:
                print(book)
            print("----------------------------------")
        else:
            print(f"\n No book found with title matching '{title}'.")

    def check_out_book(self, title):
        """Marks a book as checked out."""
        # For simplicity, we'll check out the first matching book found
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_checked_out:
                    book.is_checked_out = True
                    print(f"\n Book '{book.title}' has been successfully checked out.")
                    return
                else:
                    print(f"\n Book '{book.title}' is already checked out.")
                    return
        print(f"\n Book with title '{title}' not found.")

    def return_book(self, title):
        """Marks a checked-out book as returned."""
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_checked_out:
                    book.is_checked_out = False
                    print(f"\n Book '{book.title}' has been successfully returned.")
                    return
                else:
                    print(f"\n Book '{book.title}' was not checked out.")
                    return
        print(f"\n Book with title '{title}' not found.")

#BOOK LIBRARY

# 1. Initialize the library
my_library = Library()

# 2. Create and add some books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
book2 = Book("1984", "George Orwell", "978-0451524935")
book3 = Book("Pride and Prejudice", "Jane Austen", "978-0141439518")

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

# 3. List all books
my_library.list_books()

# 4. Search for a book
my_library.search_book("gatsby")
my_library.search_book("problem solving")

# 5. Check out a book
my_library.check_out_book("1984")

# 6. List books again to see the status change
my_library.list_books()

# 7. Try to check out the same book again
my_library.check_out_book("1984")

# 8. Return a book
my_library.return_book("1984")

# 9. List books one last time
my_library.list_books()
