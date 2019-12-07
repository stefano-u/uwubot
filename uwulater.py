import random
import re

class WordToReplace():
    def __init__(self, old, new):
        self.old = old
        self.new = new

list_words = [
    WordToReplace("father", "daddy"),
    WordToReplace("papa", "papi"),
    WordToReplace("dad", "daddy"),
    WordToReplace("mom", "mommy"),
    WordToReplace("mother", "mommy"),
    WordToReplace('l', 'w'),
    WordToReplace('r', 'w'),
    WordToReplace('u', 'wu'),
    WordToReplace("no", "nyo"),
    WordToReplace("mo", "myo"),
    WordToReplace("na", "nya"),
    WordToReplace("ni", "nyi"),
    WordToReplace("nu", "nyu"),
    WordToReplace("ne", "nye"),
    WordToReplace("anye", "ane"),
    WordToReplace("inye", "ine"),
    WordToReplace("onye", "one"),
    WordToReplace("unye", "une")
]

uwu_faces = [ 
    "OwO", "ÓwÓ", "ÕwÕ", "@w@", "ØwØ", 
    "øwø", "uwu", "☆w☆", "✧w✧", "♥w♥", 
    "◕w◕", "ᅌwᅌ", "◔w◔", "ʘwʘ", "⓪w⓪"
]

# Perform message replacement and custom text
def uwulate(message):

    # Replaces all periods with an "uwu" face
    has_period = check_period(message)
    while check_period(message):
        message = message.replace(
            '.', " `" + random.choice(words.uwu_faces) + "`", 1)

    # Replace the words in the message
    message = replace_msg(message)
    
    # Appends a uwu face if there's no period
    if not has_period:
        message = message + " `" + random.choice(uwu_faces) + "`"

    return message

# Checks if there's a period inside the message
def check_period(message):
    if "." in message:
        return True
    else:
        return False

# Replaces the words declared in list_words
def replace_msg(message): 
    for word in list_words:
        pattern = re.compile("\\b"+word.old+"\\b")
        message = pattern.sub(word.new, message)
        pattern = re.compile("\\b"+word.old.capitalize()+"\\b")
        message = pattern.sub(word.new.capitalize(), message)
    return message


