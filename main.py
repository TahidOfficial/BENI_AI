from brain import reply
from voice import speak
from listener import listen
from memory import load_memory
from apps import open_app

print("=" * 35)
print("        🤖 BENI AI")
print("=" * 35)

memory = load_memory()

if "name" in memory:
    welcome = f"Welcome back {memory['name']}!"
    print("BENI:", welcome)
    speak(welcome)

print("\nChoose Mode")
print("1. Voice")
print("2. Text")
print("3. Voice + Text")

mode = input("\nEnter choice (1/2/3): ").strip()

print("\nType or say 'bye' to exit.\n")

while True:

    if mode == "1":
        input("Press Enter to start listening...")
        user = listen()

        if not user:
            continue

    elif mode == "2":
        user = input("Oni: ")

    elif mode == "3":
        choice = input("\n[V] Voice  |  [T] Text : ").lower()

        if choice == "v":
            input("Press Enter to start listening...")
            user = listen()

            if not user:
                continue

        else:
            user = input("Oni: ")

    else:
        print("Invalid Choice!")
        break
    app = open_app(user)

    if app:
        print("BENI:", app)
        speak(app)


        if user.lower() == "bye":
            break

        continue

    answer = reply(user)

    print("BENI:", answer)
    speak(answer)

    if user.lower() == "bye":
        break