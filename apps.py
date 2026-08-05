import webbrowser
import os
import urllib.parse


def open_youtube():
    webbrowser.open("https://www.youtube.com")


def open_google():
    webbrowser.open("https://www.google.com")


def open_notepad():
    os.system("notepad")


def open_calculator():
    os.system("calc")


def open_app(text):
    text = text.lower().strip()

    # ---------- YouTube Search ----------
    if text.startswith("youtube search "):
        query = text.replace("youtube search ", "")
        url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)
        webbrowser.open(url)
        return f"YouTube par {query} search kar raha hoon."

    elif text.startswith("search youtube "):
        query = text.replace("search youtube ", "")
        url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)
        webbrowser.open(url)
        return f"YouTube par {query} search kar raha hoon."

    # ---------- Google Search ----------
    elif text.startswith("google search "):
        query = text.replace("google search ", "")
        url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
        webbrowser.open(url)
        return f"Google par {query} search kar raha hoon."

    elif text.startswith("search google "):
        query = text.replace("search google ", "")
        url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
        webbrowser.open(url)
        return f"Google par {query} search kar raha hoon."

    # ---------- Open Apps ----------
    elif "youtube" == text:
        open_youtube()
        return "YouTube khol raha hoon."

    elif "google" == text:
        open_google()
        return "Google khol raha hoon."

    elif "notepad" in text:
        open_notepad()
        return "Notepad khol raha hoon."

    elif "calculator" in text or "calc" in text:
        open_calculator()
        return "Calculator khol raha hoon."

    return None