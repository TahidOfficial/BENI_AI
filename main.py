from brain import reply

print("💙 BENI AI Started")
print("Type 'bye' to exit.\n")

while True:
    user = input("Oni: ")

    answer = reply(user)
    print("BENI:", answer)

    if user.lower() == "bye":
        break