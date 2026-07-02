print("🤖 AI Chat Assistant")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("AI: Hello! How are you?")
    elif user == "how are you":
        print("AI: I am fine. Thanks for asking!")
    elif user == "your name":
        print("AI: My name is Python AI Assistant.")
    elif user == "bye":
        print("AI: Goodbye! Have a nice day.")
        break
    else:
        print("AI: Sorry, I don't understand.")