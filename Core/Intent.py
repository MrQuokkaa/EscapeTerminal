from Database.Commands import movement_words

def resolve_intent(command, verb, modifier, target):
    if command:
        return command, verb, modifier, target
    
    if verb in movement_words:
        return "go", verb, modifier, target
    
    return None, verb, modifier, target