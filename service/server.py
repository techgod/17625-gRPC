from concurrent import futures

import grpc
import logging

import libraryobjects_pb2
import libraryservice_pb2
import libraryservice_pb2_grpc
from mock_db import library


class InventoryServicer(libraryservice_pb2_grpc.InventoryServiceServicer):
    def GetBook(self, request, context):
        if request.isbn in library:
            # Book with the given ISBN present in library, return the book details
            return libraryservice_pb2.GetBookResponse(book=library[request.isbn])
        else:
            # Book not present in library, set error
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Book Not Found.')
            return libraryservice_pb2.GetBookResponse()

    def CreateBook(self, request, context):
        # Skip if book already exists
        if request.book.isbn in library:
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details('Book with this ISBN already present in library.')

        # Create the book
        new_book = libraryobjects_pb2.Book(isbn=request.book.isbn, title=request.book.title,
                                           author=request.book.author, genre=request.book.genre,
                                           year=request.book.year)

        # Add to the library
        library[request.book.isbn] = new_book

        # Indicate that book creation is successful
        context.set_code(grpc.StatusCode.OK)
        context.set_details('Book created successfully!')


# Start gRPC server
def start_server():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    libraryservice_pb2_grpc.add_InventoryServiceServicer_to_server(
        InventoryServicer(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    start_server()
