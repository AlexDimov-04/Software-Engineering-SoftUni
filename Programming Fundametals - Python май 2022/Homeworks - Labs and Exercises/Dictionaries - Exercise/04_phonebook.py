phone_book = {}

while True:
    entry = input()
    if '-' not in entry:
        break

    name, phone = entry.split('-')
    phone_book[name] = phone

for i in range(int(entry)):
    contact = input()
    if contact in phone_book.keys():
        print(f"{contact} -> {phone_book[contact]}")
    else:
        print(f"Contact {contact} does not exist.")
