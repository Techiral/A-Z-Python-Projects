class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def search_contact(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query.lower() in contact.email.lower():
                results.append(contact)
        return results

# Example usage:
if __name__ == "__main__":
    address_book = AddressBook()

    contact1 = Contact("John Doe", "123-456-7890", "john@example.com")
    contact2 = Contact("Jane Doe", "987-654-3210", "jane@example.com")

    address_book.add_contact(contact1)
    address_book.add_contact(contact2)

    print("All Contacts:")
    address_book.view_contacts()

    print("\nSearch results for 'Jane':")
    results = address_book.search_contact("Jane")
    for result in results:
        print(f"Name: {result.name}, Phone: {result.phone}, Email: {result.email}")
