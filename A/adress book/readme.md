python address_book.py
# Creating an AddressBook instance
address_book = AddressBook()

# Adding contacts
contact1 = Contact("John Doe", "123-456-7890", "john@example.com")
contact2 = Contact("Jane Doe", "987-654-3210", "jane@example.com")
address_book.add_contact(contact1)
address_book.add_contact(contact2)

# Viewing all contacts
address_book.view_contacts()

# Searching for contacts
results = address_book.search_contact("Jane")
for result in results:
    print(f"Name: {result.name}, Phone: {result.phone}, Email: {result.email}")
