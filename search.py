from rooms import rooms

def search_customer():
    print("\n--- SEARCH CUSTOMER ---")
    
    name = input("Enter customer name: ")
    
    found = False

    for room_no, details in rooms.items():
        if details["customer"].lower() == name.lower():
            print(f"{name} is staying in Room {room_no}")
            found = True

    if not found:
        print("Customer not found")
