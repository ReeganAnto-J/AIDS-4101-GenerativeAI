import random

# Define responses based on user input
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thank you!", "Feeling great, thanks for asking!", "I'm doing well, how about you?"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "default": ["Sorry, I didn't understand that.", "Could you please rephrase that?", "I'm not sure I follow."],
}

# Function to generate response based on user input
def generate_response(user_input):
    user_input = user_input.lower()
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return random.choice(responses["default"])

# Main function to run the chatbot
def main():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = generate_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    main()    
