from brain import reply
from voice import speak
from listener import listen
from apps import open_app
from memory import load_memory

print("BENI AI Started")

memory = load_memory()

if "name" in memory:
    welcome = f"Welcome back {memory['name']}!"
    print("BENI:", welcome)
    speak(welcome)

print("Say 'bye' to exit.\n")

while True:
    input("press Enter to start listening...")
    user = listen()

    if not user:
        continue

    app = open_app(user)

    if app:
        print("BENI:", app)
        speak(app)
        continue

    answer = reply(user)

    print("BENI:", answer)
    speak(answer)

    if user.lower() == "bye":
        break