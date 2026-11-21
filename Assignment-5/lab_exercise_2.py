class Book:
    """Represents a single book in the library."""

    def __init__(self, book_id, title, author, total_copies=1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def is_available(self):
        return self.available_copies > 0

    def __str__(self):
        status = f"{self.available_copies}/{self.total_copies} available"
        return f"[{self.book_id}] {self.title} by {self.author} ({status})"


class Member:
    """Represents a registered library member."""

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"[{self.member_id}] {self.name} (Borrowed: {len(self.borrowed_books)})"


class Library:
    """Manages books, members, and issue/return transactions."""

    def __init__(self, library_name):
        self.library_name = library_name
        self.books = {}
        self.members = {}

    def add_book(self, book):
        if book.book_id in self.books:
            existing = self.books[book.book_id]
            existing.total_copies += book.total_copies
            existing.available_copies += book.total_copies
            print(f"Updated copies for '{existing.title}'. Total: {existing.total_copies}")
        else:
            self.books[book.book_id] = book
            print(f"Added book: {book.title}")

    def register_member(self, member):
        if member.member_id in self.members:
            print(f"Member ID {member.member_id} already exists.")
            return
        self.members[member.member_id] = member
        print(f"Registered member: {member.name} ({member.member_id})")

    def issue_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)

        if not member:
            print("Error: Member ID not found.")
            return
        if not book:
            print("Error: Book ID not found.")
            return
        if not book.is_available():
            print(f"Sorry, '{book.title}' is currently out of stock.")
            return
        if book_id in member.borrowed_books:
            print(f"{member.name} has already borrowed '{book.title}'.")
            return

        book.available_copies -= 1
        member.borrowed_books.append(book_id)
        print(f"Issued '{book.title}' to {member.name}.")

    def return_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)

        if not member or not book:
            print("Error: Invalid Member ID or Book ID.")
            return
        if book_id not in member.borrowed_books:
            print(f"{member.name} does not have '{book.title}' borrowed.")
            return

        member.borrowed_books.remove(book_id)
        book.available_copies += 1
        print(f"Returned '{book.title}' from {member.name}.")

    def display_catalog(self):
        print(f"\n--- {self.library_name} Catalog ---")
        if not self.books:
            print("No books in catalog.")
            return
        print(f"{'ID':<8} {'Title':<30} {'Author':<20} {'Available':<10}")
        print("-" * 72)
        for book in self.books.values():
            avail = f"{book.available_copies}/{book.total_copies}"
            print(f"{book.book_id:<8} {book.title:<30} {book.author:<20} {avail:<10}")

    def display_members(self):
        print("\n--- Registered Members ---")
        for member in self.members.values():
            borrowed_titles = [self.books[bid].title for bid in member.borrowed_books if bid in self.books]
            books_str = ", ".join(borrowed_titles) if borrowed_titles else "None"
            print(f"{member.member_id:<10} {member.name:<18} | Borrowed: {books_str}")


def seed_library(library):
    """Preloads sample books and members for immediate testing."""
    library.books["B101"] = Book("B101", "Python Crash Course", "Eric Matthes", 3)
    library.books["B102"] = Book("B102", "Clean Code", "Robert C. Martin", 2)
    library.books["B103"] = Book("B103", "Hands-On Machine Learning", "Aurelien Geron", 2)
    library.members["25BTRCL125"] = Member("25BTRCL125", "Rajeswar")
    library.members["25BTRCL102"] = Member("25BTRCL102", "Diya Nair")


def main():
    library = Library("CSE Central Library")
    seed_library(library)

    while True:
        print("\n=== Library Management System (OOP) ===")
        print("1. Display Book Catalog")
        print("2. Display Members & Borrowed Books")
        print("3. Add New Book")
        print("4. Register New Member")
        print("5. Issue Book")
        print("6. Return Book")
        print("0. Exit")

        choice = input("Enter your choice (0-6): ").strip()
        if choice == "1":
            library.display_catalog()
        elif choice == "2":
            library.display_members()
        elif choice == "3":
            bid = input("Enter Book ID (e.g., B104): ").strip().upper()
            title = input("Enter Book Title: ").strip()
            author = input("Enter Author Name: ").strip()
            try:
                copies = int(input("Enter Number of Copies: ").strip())
                if not bid or not title or not author or copies <= 0:
                    raise ValueError
                library.add_book(Book(bid, title, author, copies))
            except ValueError:
                print("Invalid book details or copy count.")
        elif choice == "4":
            mid = input("Enter Member ID: ").strip().upper()
            name = input("Enter Member Name: ").strip()
            if mid and name:
                library.register_member(Member(mid, name))
            else:
                print("Member ID and Name cannot be empty.")
        elif choice == "5":
            mid = input("Enter Member ID (e.g., 25BTRCL125): ").strip().upper()
            bid = input("Enter Book ID (e.g., B101): ").strip().upper()
            library.issue_book(mid, bid)
        elif choice == "6":
            mid = input("Enter Member ID: ").strip().upper()
            bid = input("Enter Book ID: ").strip().upper()
            library.return_book(mid, bid)
        elif choice == "0":
            print("Exiting Library Management System.")
            break
        else:
            print("Invalid choice. Please enter 0-6.")


if __name__ == "__main__":
    main()