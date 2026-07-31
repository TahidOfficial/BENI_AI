from brain import reply
from voice import speak
from apps import open_app
from memory import load_memory, save_memory

print("BENI AI Started")
memory = load_memory()
if "name" in memory:
    welcome = f"Welcome back {memory['name']}!"
    print("BENI:", welcome)
    speak(welcome)

'''if "game" in memory:
    game = f"I remember your favorite game is {memory['game']}."
    print("BENI:", game)
    speak(game)'''
print("Type 'bye' to exit.\n")

while True:
    user = input("Oni: ")
    memory = load_memory()

    app = open_app(user)

    if app:
        print("BENI:", app)
        continue

    answer = reply(user)
    print("BENI:", answer)
    speak(answer)

    if user.lower() == "bye":
        break