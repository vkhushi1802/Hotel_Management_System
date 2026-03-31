from rooms import rooms
from rooms import save_rooms


def checkout():
    print("\n---CHECKOUT---")

    room_no = input("Enter room number: ")

    #check if room exists
    if room_no in rooms:

        # Check if occupied
        if rooms[room_no]["status"] == "occupied":

            name= rooms[room_no]["customer"]
            days= rooms[room_no]["days"]
            rate = 1000
            
            total = days * rate
            
            print(f"Total bill for Room {room_no}: ₹{total}")
            
            # Free the room
            rooms[room_no]["status"] = "available"
            rooms[room_no]["customer"]= ""
            rooms[room_no]["days"]=0

            save_rooms(rooms)

            print("Checkout successful. Room is now available.")
        
        else:
            print("Room is already empty!")

    else:
        print("Invalid room number!")





    