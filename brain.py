from datetime import datetime

def reply(text):
    text = text.lower()

    if "hello" in text or "hi" in text:
        return "Hello Oni! 💙"

    elif "how are you" in text:
        return "Main bilkul theek hoon. Tum kaise ho Oni? 😊"

    elif "who are you" in text:
        return "Main BENI hoon, tumhari personal AI assistant. 🤖"

    elif "your name" in text or text == "name":
        return "Mera naam BENI hai. 💙"

    elif "thank" in text:
        return "Welcome Oni! 😊"

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

    elif "bye" in text:
        return "Bye Oni! Phir milte hain. 💙"

    else:
        return "Sorry Oni, mujhe abhi ye command samajh nahi aayi. 😅"