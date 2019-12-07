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
    WordToReplace('l', 'w', False),
    WordToReplace('r', 'w', False),
    WordToReplace('u', 'wu', False),
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


