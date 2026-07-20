def chatbot():
    print("===== Simple Chatbot =====")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi! How are you?")
        elif user == "hi":
            print("Bot: Hello!")
        elif user == "how are you":
            print("Bot: I'm fine, thank you!")
        elif user == "your name":
            print("Bot: I am CodeAlpha Chatbot.")
        elif user == "what can you do":
            print("Bot: I can answer simple questions.")
        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I don't understand.")

chatbot()