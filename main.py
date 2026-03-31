from rooms import view_rooms
from booking import book_room
from billing import checkout

def menu():
    while True:
        print("\n---Hotel Management System-----")
        print("1. View Rooms")
        print("2. Book Room")
        print("3. Checkout")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_rooms()
        elif choice == '2':
            book_room()
        elif choice == '3':
            checkout()
        elif choice == '4':
            print("Exiting system...")
            break
        else:
            print("Invalid choice")
    
menu()