from inventory_client import InventoryAPI


# Function to retrieve the titles of a list of books given their ISBNs
def get_book_titles(inventory_client, isbn_list):
    # Create a list of titles
    titles = []
    for isbn in isbn_list:
        # Query for book details
        book_response = inventory_client.get_book(isbn)
        # Add book title to list of all titles
        titles.append(book_response.book.title)
    return titles


if __name__ == '__main__':
    inventoryAPI = InventoryAPI('localhost', 50051)
    # Some hardcoded ISBNs present in database
    isbn_list = ["9780062875914", "9780771038518"]
    book_titles = get_book_titles(inventoryAPI, isbn_list)
    for title in book_titles:
        print(title)
