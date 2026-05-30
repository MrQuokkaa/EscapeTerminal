commands = {
    "go": {
        "go",
        "walk",
        "move",
        "travel",
    },
    "take": {
        "take",
        "grab",
        "pick",
        "pickup"
    },
    "use": {
        "use",
        "activate",
        "interact",
    },
    "touch": {
        "touch",
    },
    "open": {
        "open",
    },
    "push": {
        "push",
        "press"
    },
    "pull": {
        "pull",
    },
    "dodge": {
        "dodge",
        "dash",
        "roll"
    },
    "hide": {
        "hide",
        "evade"
    }
}

modifiers = {
    "slow": {
        "crawl",
        "crouch"
    },
    "stealth": {
        "sneak",
        "creep"
    },
    "fast": {
        "run",
        "drive",
        "ride",
        "fly",
    }
}

movement_words = {
        "go",
        "walk",
        "move",
        "travel",
        "sneak",
        "creep",
        "run",
        "drive",
        "ride",
        "fly",
        "crawl",
        "crouch"
}

filler_words = {
    "to", "into", "on", "at", "the", "a", "an", "behind", "through"
}

def command_map(source):
    return {word: key for key, words in source.items() for word in words}

command_lookup = command_map(commands)
modifier_lookup = command_map(modifiers)