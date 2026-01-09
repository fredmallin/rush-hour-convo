import time

def printConversation():
    conversation = [
        ("Blue", "Who are you?", 1),
        ("Yellow", "Yu.", 0.03),
        ("Blue", "No, not me — YOU!", 0.9),
        ("Yellow", "Yes. I'm Yu.", 1),
        ("Blue", "Just answer the damn questions. Who are you?", 1.9),
        ("Yellow", "I have told you.", 1.3),
        ("Blue", "Are you deaf?", 1.6),
        ("Yellow", "No. Yu is blind.", 1.5),
        ("Blue", "I'm not blind — YOU are blind!", 1.5),
        ("Yellow", "It is what I just said.", 0.7),
        ("Blue", "You just said WHAT?", 0.5),
        ("Yellow", "I did not say what. I said Yu.", 1.8),
        ("Blue", "That’s what I’m asking you!", 1.8),
        ("Yellow", "And Yu is answering.", 1),
        ("Blue", "Shut up, you!", 1),
        ("Yellow", "Yes?", 1),
        ("Blue", "Not YOU — HIM! What’s your name?", 1),
        ("Yellow", "Mi.", 1.5),
        ("Blue", "Yes, you!", 1),
        ("Yellow", "I am Mi.", 0.5),
        ("Blue", "He’s Mi… and I’m Yu.", 2)
    ]

    for color, text, pause in conversation:
        if color == "Blue":
            print(f"\033[94m{text}\033[0m") 
        else:
            print(f"\033[93m{text}\033[0m")  
        time.sleep(pause)

printConversation()
