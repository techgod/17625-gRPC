# A mock db storing some hardcoded data
from libraryobjects_pb2 import Book

# A few books
book1 = Book(
    isbn="0-7475-3269-9", title="Harry Potter and the Philosopher's Stone",
    author="J. K. Rowling", genre=Book.FANTASY,
    year=1999)

book2 = Book(
    isbn="9780771038518", title="Sapiens: A Brief History of Humankind",
    author="Yuval Noah Harari", genre=Book.NONFICTION,
    year=2015)

# The books are present in a 'library' dictionary
# More books can be added at runtime using the CreateBook function
library = {"0-7475-3269-9": book1, "9780771038518": book2}
