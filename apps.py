import webbrowser
import os

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_google():
    webbrowser.open("https://www.google.com")

def open_notepad():
    os.system("notepad")

def open_calculator():
    os.system("calc")

def open_app(text):
    text = text.lower()

    if "youtube" in text:
        webbrowser.open("https://www.youtube.com")
        return "YouTube khol raha hoon. "

    elif "google" in text:
        webbrowser.open("https://www.google.com")
        return "Google khol raha hoon. "

    elif "notepad" in text:
        os.system("notepad")
        return "Notepad khol raha hoon. "

    elif "calculator" in text or "calc" in text:
        os.system("calc")
        return "Calculator khol raha hoon. "
    return None