from apps import open_youtube, open_google, open_notepad, open_calculator
from datetime import datetime
from memory import load_memory, save_memory


def reply(text):
    text = text.lower().strip()

    memory = load_memory()

    # Greetings
    if any(word in text for word in [
        "hello", "hi", "hey",
        "namaste", "namaskar",
        "salaam", "assalamualaikum"
    ]):
        return "Hello Oni! Batao kya karna hai?"

    # How are you
    elif "how are you" in text or "kaise ho" in text or "kese ho" in text:
        return "Main bilkul theek hoon. Tum kaise ho Oni?"

    # Who are you
    elif "who are you" in text or "tum kaun ho" in text or "tum kon ho" in text:
        return "Main BENI hoon, tumhari personal AI assistant."

    # Name
    elif "your name" in text or "tumhara naam" in text or text == "name":
        return "Mera naam BENI hai."

    # Thanks
    elif "thank" in text or "thanks" in text or "shukriya" in text:
        return "Welcome Oni!"

    # Time
    elif "time" in text or "kitna baje" in text or "samay" in text:
        return datetime.now().strftime("Abhi time hai %I:%M %p")

    # Date
    elif "date" in text or "tarikh" in text:
        return datetime.now().strftime("Aaj ki date %d-%m-%Y hai")

    # Calculator
    elif text.startswith("calculate "):
        try:
            question = text.replace("calculate ", "")
            answer = eval(question)
            return f"Answer: {answer}"
        except:
            return "Calculation samajh nahi aayi."

    # Google
    elif "google" in text:
        open_google()
        return "Google khol raha hoon."

    # YouTube
    elif "youtube" in text:
        open_youtube()
        return "YouTube khol raha hoon."

    # Notepad
    elif "notepad" in text:
        open_notepad()
        return "Notepad khol raha hoon."

    # Calculator App
    elif "calculator" in text or "calc" in text:
        open_calculator()
        return "Calculator khol raha hoon."

    # Save Name
    elif text.startswith("my name is "):
        name = text.replace("my name is ", "").strip()
        memory["name"] = name
        save_memory(memory)
        return f"Nice to meet you {name}! Main yaad rakhunga."

    # Save Favourite
    elif text.startswith("i like "):
        game = text.replace("i like ", "").strip()
        memory["game"] = game
        save_memory(memory)
        return f"Achha! Mujhe yaad rahega ki tumhe {game} pasand hai."

    # Remember
    elif text.startswith("remember "):
        info = text.replace("remember ", "")

        if "=" in info:
            key, value = info.split("=", 1)
            memory[key.strip()] = value.strip()
            save_memory(memory)
            return f"Theek hai Oni, maine {key.strip()} yaad rakh liya."

        else:
            return "Format likho: remember name=Oni"

    # Recall
    elif text.startswith("what is "):
        key = text.replace("what is ", "").strip()

        if key in memory:
            return f"{key} = {memory[key]}"
        else:
            return "Ye mujhe yaad nahi hai."

    # Bye
    elif "bye" in text or "goodbye" in text:
        return "Bye Oni! Phir milte hain."

    # Default
    else:
        return "Sorry Oni, mujhe samajh nahi aaya."