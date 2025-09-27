# Mini Contact Book

def add_contact(name, phone):
    with open("contacts.txt", "a") as f:
        f.write(f"{name},{phone}\n")

def show_contacts():
    try:
        with open("contacts.txt", "r") as f:
            for line in f:
                name, phone = line.strip().split(",")
                print(f"Name: {name}, Phone: {phone}")
    except FileNotFoundError:
        print("No contacts found. Add one first!")

# Example run
add_contact("Alice", "12345")
add_contact("Bob", "67890")
show_contacts()
