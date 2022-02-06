def speak_cat():
    print("Meow")

def speak_dog():
    print("Woof")


def speak(pet_speech):
    """Dynamically dispatches the speak method at runtime"""
    pet_speech()

speak(speak_cat)
speak(speak_dog)