from apps import open_youtube, open_google, open_notepad, open_calculator
from datetime import datetime
from memory import load_memory, save_memory

def reply(text):
    text = text.lower()

    memory = load_memory()

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
        return "Opening YouTube..."

    elif "open google" in text:
        open_google()
        return "Opening Google..."

    elif "open notepad" in text:
        open_notepad()
        return "Opening Notepad..."

    elif "open calculator" in text:
        open_calculator()
        return "Opening Calculator..."

    elif text.startswith("my name is "):
        name = text.replace("my name is ", "").strip()

        memory["name"] = name
        save_memory(memory)

        return f"Nice to meet you {name}! Main yaad rakhunga. "

    elif text.startswith("i like "):
        game = text.replace("i like ", "").strip()

        memory["game"] = game
        save_memory(memory)

        return f"Achha! Mujhe yaad rahega ki tumhe {game} pasand hai."

    elif text.startswith("remember "):
        info = text.replace("remember ", "")

        if "=" in info:
            key, value = info.split("=", 1)

            memory[key.strip()] = value.strip()
            save_memory(memory)

            return f"Theek hai Oni, maine {key.strip()} yaad rakh liya."

        else:
            return "Format likho: remember name=Oni"

    elif text.startswith("what is "):
        key = text.replace("what is ", "").strip()

        if key in memory:
            return f"{key} = {memory[key]}"
        else:
            return "Ye mujhe yaad nahi hai."

    elif "bye" in text:
        return "Bye Oni! Phir milte hain."

    else:
        return "Sorry Oni, mujhe abhi ye command samajh nahi aayi. 😒"