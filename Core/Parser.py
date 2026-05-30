from Functions import normalize
from Database.Commands import filler_words, modifier_lookup, command_lookup

def parse_input(text):
    words = normalize(text).split()
    words = [w for w in words if w not in filler_words]

    if not words:
        return None, None, None, None
    
    raw_verb = None
    modifier = None
    command = None

    remaining = []

    for w in words:
        if w in modifier_lookup:
            modifier = modifier_lookup[w]
            raw_verb = w
        else:
            remaining.append(w)

    words = remaining
    remaining = []
    
    for w in words:
        if w in command_lookup:
            command = command_lookup[w]
            raw_verb = w
        else:
            remaining.append(w)
    
    words = remaining

    target = " ".join(words) if words else None

    return command, raw_verb, modifier, target