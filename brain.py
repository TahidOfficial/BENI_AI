from apps import open_youtube, open_google, open_notepad, open_calculator
from datetime import datetime

def reply(text):
    text = text.lower()

    if "hello" in text or "hi" in text:
        return "Bolo Oni!"

    elif "how are you" in text or "kaise ho" in text:
        return "Main bilkul theek hoon. Tum kaise ho Oni?"

    elif "who are you" in text:
        return "Main BENI hoon, tumhari personal AI assistant. 🤖"

    elif "your name" in text or text == "name":
        return "Mera naam BENI hai."

    elif "thank" in text:
        return "Welcome Oni!"

    elif "time" in text:
        return datetime.now().strftime("Abhi time hai %I:%M %p")

    elif "date" in text:
        return datetime.now().strftime("Aaj ki date %d-%m-%Y hai")

    elif text.startswith("calculate "):
        try:
            question = text.replace("calculate ", "")
            answer = eval(question)
            return f"Answer: {answer}"
        except:
            return "Calculation samajh nahi aayi."

    elif "open youtube" in text:
         open_youtube()
         return "Opening YouTube... "
    
    elif "open google" in text:
         open_google()
         return "Opening Google... "

    elif "open notepad" in text:
        open_notepad()
        return "Opening Notepad... "

    elif "open calculator" in text:
        open_calculator()
        return "Opening Calculator... "

    elif "bye" in text:
        return "Bye Oni! Phir milte hain."

    else:
        return "Sorry Oni, mujhe abhi ye command samajh nahi aayi. 😒"