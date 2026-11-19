contacts = {
    "Ana": {"phone": "0722000001", "email": "ana@example.com"},
    "Mihai": {"phone": "0722000002", "email": "mihai@example.com"},
}

MENU = """
1. List contacts
2. Add contact
3. Search by name
4. Delete contact
5. Quit"""


def find_key(book, name):
    target = name.strip().lower()
    for key in book:
        if key.lower() == target:
            return key
    return None


def list_contacts(book):
    if not book:
        print("No contacts yet.")
        return
    rows = [(name, c["phone"], c["email"]) for name, c in book.items()]
    rows.sort(key=lambda r: r[0].lower())
    headers = ("Name", "Phone", "Email")
    widths = [max(len(headers[i]), *(len(r[i]) for r in rows)) for i in range(3)]
    print("  ".join(h.ljust(w) for h, w in zip(headers, widths)).rstrip())
    for row in rows:
        print("  ".join(v.ljust(w) for v, w in zip(row, widths)).rstrip())


def add_contact(book):
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    existing = find_key(book, name)
    if existing is not None:
        answer = input(f"'{existing}' already exists. Overwrite? (y/n): ").strip().lower()
        if answer not in ("y", "yes"):
            print("Cancelled.")
            return
        del book[existing]
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    book[name] = {"phone": phone, "email": email}
    print(f"Saved '{name}'.")


def search_contact(book):
    name = input("Search name: ")
    key = find_key(book, name)
    if key is None:
        print(f"No contact named '{name.strip()}'.")
        return
    print(f"{key} | {book[key]['phone']} | {book[key]['email']}")


def delete_contact(book):
    name = input("Delete name: ")
    key = find_key(book, name)
    if key is None:
        print(f"No contact named '{name.strip()}' to delete.")
        return
    del book[key]
    print(f"Deleted '{key}'.")


def to_list(book):
    return [{"name": n, **c} for n, c in book.items()]


def find_in_list(items, name):
    target = name.strip().lower()
    for item in items:
        if item["name"].lower() == target:
            return item
    return None


def main():
    while True:
        print(MENU)
        choice = input("Choose: ").strip().lower()
        if choice in ("5", "quit"):
            print("Goodbye.")
            break
        elif choice == "1":
            list_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        else:
            print("Invalid option. Choose 1-5 or 'quit'.")


if __name__ == "__main__":
    main()