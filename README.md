## 17625 - Assignment 3 & 4
### gRPC
<br>

##### Execution Steps
Recommended: Create a Python 3.5+ virtual environment
1. Install Dependencies
    ```
    pip install -r requirements.txt
    ```
2. Start server
    ```
    python service/server.py
    ```
   Endpoint: ```localhost:50051```
3. Run client
    ```
    python client/get_book_titles.py
    ```
4. Run tests
    ```
    python -m unittest client/test.py
    ```