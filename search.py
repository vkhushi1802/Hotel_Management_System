from rooms import rooms

def search_customer():
    print("\n---Search Customer")

    name = input("Enter customern name: ")

    found = False

    for room_no, details in rooms.items():
        if details[]