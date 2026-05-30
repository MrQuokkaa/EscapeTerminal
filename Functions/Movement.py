from Database.Locations import locations
from Core.Parser import verb

def go_to(target, modifier=None):
    if not target:
        print("Where?")
        return
    
    if target in locations:
        print(f"You {verb} to {locations}")
        locations[target]()
    else:
        print("That destination doesn't exist.")