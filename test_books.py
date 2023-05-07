
# Request with basic auth
import requests

# response = requests.get("http://localhost:8000/books")
# print(response.json())

# Create a book
response = requests.post(
    "http://127.0.0.1:8001/books",
    json={
        "title": "The Great Gatsby 4",
        "author": "Fuck. Scott Fitzgerald",
        "pages_count": 55,
    },
)

# update book
# response = requests.put(
#     "http://127.0.0.1:8001/books/7",
#     json={
#         "title": "The Great Gatsby 3",
#         "author": "Fuck. Scott Fitzgerald",\
#         "pages_count": 55,
#     },
# )
#delete book
# response = requests.delete(
#     "http://127.0.0.1:8001/books/delete/2",
#     )
print(response.text)
print(response)
