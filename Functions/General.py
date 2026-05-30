def normalize(text):
    return text.strip().lower().replace(" ", "")

def get_input(prompt="> "):
    return normalize(input(prompt))