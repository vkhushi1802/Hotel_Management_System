from rooms import rooms, save_rooms



def book_room():
    print("\n--- BOOK ROOM---")

    room_no = input("Enter room number: ")

    #check if room exists
    if room_no in rooms:
        #check if available
        if rooms[room_no]["status"] == "available":
            name = input("Enter customer name: ")
            days = int(input("Enter number of days: "))

            rooms[room_no]["status"] = "occupied"
            rooms[room_no]["customer"]= name
            rooms[room_no]["days"] = days
            save_rooms(rooms)
            print(f"Room {room_no} successfully booked for{name}")

        else:
            print("Room is already occupied!")

    else:
        print("Invalid room number!")

