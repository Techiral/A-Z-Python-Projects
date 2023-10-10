import sqlite3

# Create a database and connect to it
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        isbn TEXT,
        quantity INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        book_id INTEGER,
        user_id INTEGER,
        borrow_date DATE,
        return_date DATE,
        FOREIGN KEY (book_id) REFERENCES books(id),
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')

# Functions for library management
def add_book(title, author, isbn, quantity):
    cursor.execute('INSERT INTO books (title, author, isbn, quantity) VALUES (?, ?, ?, ?)', (title, author, isbn, quantity))
    conn.commit()

def remove_book(book_id):
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()

def list_books():
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    for book in books:
        print(book)

def add_user(name, email):
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()

def remove_user(user_id):
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()

def list_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    for user in users:
        print(user)

def borrow_book(book_id, user_id, borrow_date, return_date):
    cursor.execute('INSERT INTO transactions (book_id, user_id, borrow_date, return_date) VALUES (?, ?, ?, ?)', (book_id, user_id, borrow_date, return_date))
    cursor.execute('UPDATE books SET quantity = quantity - 1 WHERE id = ?', (book_id,))
    conn.commit()

def return_book(transaction_id):
    cursor.execute('DELETE FROM transactions WHERE id = ?', (transaction_id,))
    conn.commit()

# Sample usage
add_book('Python Crash Course', 'Eric Matthes', '978-1593276034', 5)
add_book('Clean Code', 'Robert C. Martin', '978-0132350884', 3)
add_user('John Doe', 'johndoe@email.com')
borrow_book(1, 1, '2023-10-10', '2023-11-10')
list_books()
list_users()

# Close the database connection when done
conn.close()