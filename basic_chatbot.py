def get_response(message):
    """Return a predefined response for a supported message."""
    message = message.strip().lower()

    if message == "hello":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Try: hello, how are you, or bye."


def main():
    """Run the chatbot until the user says goodbye."""
    print("Basic Python Chatbot")
    print("Type 'hello', 'how are you', or 'bye' to chat.")

    while True:
        user_message = input("You: ")
        response = get_response(user_message)
        print("Bot:", response)

        if user_message.strip().lower() == "bye":
            break


if __name__ == "__main__":
    main()
