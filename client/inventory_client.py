import grpc
import os
import sys

# Add path so modules can be imported across folders
sys.path.append(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))))

from service.libraryservice_pb2 import CreateBookRequest, GetBookRequest
from service.libraryservice_pb2_grpc import InventoryServiceStub
from service.libraryobjects_pb2 import Book


class InventoryAPI:
    def __init__(self, url=None, port=None):
        if url is None:
            # URL is not provided; we will not be creating a live server.
            self.channel = None
        else:
            # Open channel and create stub
            self.channel = grpc.insecure_channel(url + ":" + str(port))
            self.stub = InventoryServiceStub(self.channel)

    def __del__(self):
        if self.channel is not None:
            # Close channel only if it was opened
            self.channel.close()

    def create_book(self, isbn, title=None, author=None, year=None, genre=None):
        # Create a new book
        response = self.stub.CreateBook(CreateBookRequest(
            book=Book(isbn=isbn, title=title, author=author, year=year, genre=genre)))
        return response

    def get_book(self, isbn):
        # Fetch book details
        response = self.stub.GetBook(GetBookRequest(isbn=isbn))
        return response
