# Library Books and Lends API Example
## Using Django Rest Framework and DRF Extensions (for nested routes)

### Requirements
Python 3.6.x

### Installation
pip install -r requirements.txt

### Running
python manage.py runserver
server will be available at http://127.0.0.1:8000/

### Routes
GET /client - Lists all clients
GET /client/{client_id}/books - Lists all books currently lent to client, with current fine and interest information
GET /books - Lists all books and availability
POST /books/{book_id}/reserve ( body: {client_id: <client_id> } ) - Lend book to the provided client, if its available

### Django Admin
Browser interface to view the data and create new entities by hand.
/admin 
user: admin
password: admin

