#dictionary to store room status
import json

#Load room data from file
def load_rooms():
    with open("rooms.json", "r") as file:
        return json.load(file)
    
#Save room data to file
def save_rooms(room):
    with open("rooms.json", "w") as file:
        return json.dump(rooms, file)

#load rooms at start
rooms = load_rooms()



def view_rooms():
    print("\n----Room Status-----")
    for room_no,details in rooms.items():
        status = details["status"]
        print(f"Rooom {room_no}: {status}")