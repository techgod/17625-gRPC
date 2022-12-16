import unittest
from unittest.mock import Mock

# Add path so modules can be imported across folders
import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import get_book_titles
from inventory_client import InventoryAPI
from service.libraryobjects_pb2 import Book
from service.libraryservice_pb2 import GetBookResponse


class TestLibraryClient(unittest.TestCase):
    def verify(self, api, isbn_list, expected_title_list):
        # Call get_book_titles, passing in the mocked API
        titles = get_book_titles.get_book_titles(api, isbn_list)

        # Check that the size of the returned list is as expected
        self.assertEqual(len(isbn_list), len(expected_title_list))

        # Check that all the titles extracted are as expected
        for i in range(len(titles)):
            self.assertEqual(titles[i], expected_title_list[i])

    # Test 1 - Using Mock Server
    def test_get_book_titles_mock(self):
        # Build Test Data
        isbn1 = "978-1847941831"
        title1 = "Atomic Habits"
        book1 = Book(
            isbn=isbn1, title=title1,
            author="James Clear", genre=Book.NONFICTION,
            year=2018)

        isbn2 = "9780771038518"
        title2 = "Steve Jobs"
        book2 = Book(
            isbn=isbn2, title=title2,
            author="Walter Isaacson", genre=Book.BIOGRAPHY,
            year=2011)

        test_lib = {isbn1: book1, isbn2: book2}

        # Mock the API
        api = Mock()

        # Setup a side_effect for dynamic return values
        api.get_book.side_effect = lambda k: GetBookResponse(book=test_lib[k])

        # Final inputs
        isbn_list = [isbn1, isbn2]
        expected_title_list = [title1, title2]

        # verify assertions
        self.verify(api, isbn_list, expected_title_list)

    # Test 2 - Using Live Server
    def test_get_book_titles_live(self):
        # Get access to the live API
        api = InventoryAPI('localhost', 50051)

        # Choose two ISBNs to query the database
        isbn_list = ["9780062875914", "9780771038518"]

        # The titles for the corresponding books
        expected_title_list = ["And Then There Were None", "Sapiens: A Brief History of Humankind"]

        # Verify that we get these exepected values using our live server
        self.verify(api, isbn_list, expected_title_list)
