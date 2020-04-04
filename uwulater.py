import random
import re

class WordToReplace():
    def __init__(self, old, new, is_word):
        # Word to be replaced
        self.old = old
        # Word to replace old word
        self.new = new
        # Checks if its a word (ex. father) or a letter/syllable (ex. l, no, mo, na)
        self.is_word = is_word

list_words = [
    WordToReplace("father", "daddy", True),
    WordToReplace("papa", "papi", True),
    WordToReplace("dad", "daddy", True),
    WordToReplace("mom", "mommy", True),
    WordToReplace("mother", "mommy", True),
    WordToReplace("l", "w", False),
    WordToReplace("r", "w", False),
    WordToReplace("u", "wu", False),
    WordToReplace("s", "sh", False),
    WordToReplace("no", "nyo", False),
    WordToReplace("mo", "myo", False),
    WordToReplace("na", "nya", False),
    WordToReplace("ni", "nyi", False),
    WordToReplace("nu", "nyu", False),
    WordToReplace("ne", "nye", False),
    WordToReplace("anye", "ane", False),
    WordToReplace("inye", "ine", False),
    WordToReplace("onye", "one", False),
    WordToReplace("unye", "une", False)
]

uwu_faces = [ 
    "OwO", "ÓwÓ", "ÕwÕ", "@w@", "ØwØ", 
    "øwø", "uwu", "☆w☆", "✧w✧", "♥w♥", 
    "◕w◕", "ᅌwᅌ", "◔w◔", "ʘwʘ", "⓪w⓪"
]

# Perform message replacement and custom text
def uwulate(message):

    # Replaces all periods with an "uwu" face
    ends_period = message[len(message) - 1:] == "."

    new_str = ""
    for index, char in enumerate(message):
        # Replace any period, not adjacent to other periods, with "uwu"
        if char == "." and message[index - 1] != "." and message[index + 1] != ".":
            new_str = new_str + " " + random.choice(uwu_faces)
        # Add a "uwu" before any newline
        elif char == "\n":
            new_str = new_str + " " + random.choice(uwu_faces) + char
        else:
            new_str = new_str + char
    message = new_str.lower()

    # Replace the words in the message
    message = replace_msg(message)
    
    # Appends a uwu face if it doesn't finish on a period
    if not ends_period:
        message = message + " " + random.choice(uwu_faces)

    return message

# Replaces the words declared in list_words
def replace_msg(message): 
    for word in list_words:
        if (word.is_word):
            pattern = re.compile("\\b"+word.old+"\\b")
            message = pattern.sub(word.new, message)
            pattern = re.compile("\\b"+word.old.capitalize()+"\\b")
            message = pattern.sub(word.new.capitalize(), message)
        else:
            pattern = re.compile(word.old)
            message = pattern.sub(word.new, message)
            pattern = re.compile(word.old.capitalize())
            message = pattern.sub(word.new.capitalize(), message)
    return message
