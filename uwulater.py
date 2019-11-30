import random 
import time

def uwulate(message):
    has_period = check_period(message)

    message = message.replace('L', 'W')
    message = message.replace('R', 'W')
    message = message.replace('l', 'w')
    message = message.replace('r', 'w')
    message = message.replace('u', 'wu')
    message = message.replace("no", "nyo")
    message = message.replace("mo", "myo")
    message = message.replace("No", "Nyo")
    message = message.replace("Mo", "Myo")
    message = message.replace("na", "nya")
    message = message.replace("ni", "nyi")
    message = message.replace("nu", "nyu")
    message = message.replace("ne", "nye")
    message = message.replace("anye", "ane")
    message = message.replace("inye", "ine")
    message = message.replace("onye", "one")
    message = message.replace("unye", "une")

    uwu_faces = [
        "OwO",
        "ÓwÓ",
        "ÕwÕ",
        "@w@",
        "ØwØ",
        "øwø",
        "uwu",
        "☆w☆",
        "✧w✧",
        "♥w♥",
        "◕w◕",
        "ᅌwᅌ",
        "◔w◔",
        "ʘwʘ",
        "⓪w⓪"
    ]

    while check_period(message):
        message = message.replace('.', " `" + random.choice(uwu_faces) + "`", 1)

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
