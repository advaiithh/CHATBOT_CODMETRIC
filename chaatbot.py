def chatbot_response(user_input):
    user_input = user_input.lower()

    if any(greet in user_input for greet in ["hi", "hello", "hey"]):
        return "Hello! How can I assist you today?"

    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm functioning perfectly!"

    elif "what is your name" in user_input or "what's your name" in user_input:
        return "I'm CodmetricBot, your rule-based chatbot assistant."

    elif any(bye in user_input for bye in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a great day ahead."

    elif "who created you" in user_input or "who made you" in user_input:
        return "I was created by Advaith, as part of the Codmetric AI Internship."

    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! If you have any more questions, feel free to ask."

    elif "help" in user_input:
        return "Sure! You can ask me things like 'What's your name?', 'How are you?', or just say 'hi'."

    else:
        return "I'm sorry, I didn't understand that. Try asking something else."


def main():
    print("CodmetricBot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"CodmetricBot: {response}")
        if "bye" in user_input.lower():
            break


if __name__ == "__main__":
    main()
