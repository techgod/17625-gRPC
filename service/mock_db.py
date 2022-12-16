# A mock db storing some hardcoded data
from libraryobjects_pb2 import Book

# A few books
isbn1 = "9780062875914"
book1 = Book(
    isbn=isbn1, title="And Then There Were None",
    author="Agatha Christie", genre=Book.MYSTERY,
    year=1944)

isbn2 = "9780771038518"
book2 = Book(
    isbn=isbn2, title="Sapiens: A Brief History of Humankind",
    author="Yuval Noah Harari", genre=Book.NONFICTION,
    year=2015)

# The books are present in a 'library' dictionary
# More books can be added at runtime using the CreateBook function
library = {isbn1: book1, isbn2: book2}
