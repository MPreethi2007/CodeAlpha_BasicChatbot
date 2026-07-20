def chatbot():
    print("=" * 50)
    print("        Welcome to Python Chatbot")
    print("=" * 50)
    print("Type 'bye' to end the conversation.\n")

    while True:
        user = input("You: ").strip().lower()

        if user in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]:
            print("Bot: Hello! Nice to meet you. How can I help you today?")

        elif user in ["how are you", "how are you?"]:
            print("Bot: I'm doing great! Thanks for asking. How about you?")

        elif user in ["i am fine", "i'm fine", "fine", "good", "great"]:
            print("Bot: That's wonderful to hear!")

        elif user in ["what is your name", "who are you", "your name"]:
            print("Bot: My name is Python Chatbot. I am a simple rule-based chatbot.")

        elif user in ["who made you", "who created you", "developer"]:
            print("Bot: I was created by M Preethi using Python.")

        elif user in ["what can you do", "help", "features"]:
            print("Bot: I can answer basic questions, greet you,")
            print("     tell the current time, perform simple calculations,")
            print("     and have a small conversation with you.")

        elif user == "time":
            from datetime import datetime
            print("Bot: Current Time:", datetime.now().strftime("%I:%M %p"))

        elif user == "date":
            from datetime import datetime
            print("Bot: Today's Date:", datetime.now().strftime("%d-%m-%Y"))

        elif user == "python":
            print("Bot: Python is a powerful, easy-to-learn programming language.")

        elif user == "java":
            print("Bot: Java is an object-oriented programming language widely used for application development.")

        elif user == "c":
            print("Bot: C is one of the oldest and fastest programming languages.")

        elif user == "ai":
            print("Bot: Artificial Intelligence enables machines to perform tasks that normally require human intelligence.")

        elif user == "machine learning":
            print("Bot: Machine Learning is a branch of AI where computers learn from data.")

        elif user == "thank you" or user == "thanks":
            print("Bot: You're welcome! Happy to help.")

        elif user == "bye":
            print("Bot: Goodbye! Have a wonderful day.")
            break

        elif user == "tell me a joke":
            print("Bot: Why do programmers prefer dark mode?")
            print("Bot: Because light attracts bugs!")

        elif user == "motivate me":
            print("Bot: Success comes from consistency.")
            print("Bot: Keep learning and never stop practicing!")

        elif user == "tell me a fact":
            print("Bot: Python was created by Guido van Rossum and released in 1991.")

        elif user == "calculator":
            print("Bot: Enter two numbers.")
            try:
                num1 = float(input("First Number: "))
                op = input("Operator (+ - * /): ")
                num2 = float(input("Second Number: "))

                if op == "+":
                    print("Bot:", num1 + num2)
                elif op == "-":
                    print("Bot:", num1 - num2)
                elif op == "*":
                    print("Bot:", num1 * num2)
                elif op == "/":
                    if num2 != 0:
                        print("Bot:", num1 / num2)
                    else:
                        print("Bot: Division by zero is not allowed.")
                else:
                    print("Bot: Invalid operator.")
            except:
                print("Bot: Invalid input.")

        elif user == "weather":
            print("Bot: Sorry, I cannot access live weather information.")

        elif user == "favorite language":
            print("Bot: I like Python because it is simple and powerful!")

        elif user == "your hobby":
            print("Bot: My hobby is helping people learn programming.")

        elif user == "bye bye":
            print("Bot: See you soon! Take care.")
            break

        else:
            print("Bot: Sorry, I didn't understand that.")
            print("Bot: Try asking about Python, Java, AI, time, date, calculator, joke, fact, or motivation.")

chatbot()
