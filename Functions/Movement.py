from Database.Locations import places

def go_to(place_name):
    place_name = place_name.lower().strip()

    if place_name in places:
        places[place_name]()
    else:
        print("That place doesn't exist.")