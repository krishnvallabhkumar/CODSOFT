import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    if re.search(r'\bhello\b|\bhi\b|\bhey\b', user_input):
        return "Hello, I'm your friendly rule-based chatbot. How can I help you today"
    
    elif re.search(r'\bhow are you\b', user_input):
        return "I'm doing great, thank you for asking, How about you"
    
    elif re.search(r'\bname\b', user_input):
        return "I am a simple AI chatbot created for the CodSoft internship."
    
    elif re.search(r'\bhelp\b', user_input):
        return "I can answer simple questions like 'How are you', 'What is your name', or just say hello"
    
    elif re.search(r'\bbye\b|\bgoodbye\b', user_input):
        return "Goodbye, Have a wonderful day"
    
    elif re.search(r'\bweather\b', user_input):
        return "I don't have real-time access to weather data yet, but it's always sunny in the digital world"

    else:
        return "I'm sorry, I don't quite understand that. Could you try rephrasing (Type 'help' to see what I can do)"

def main():
    print("Chatbot: Hello, Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if re.search(r'\bbye\b|\bgoodbye\b', user_input.lower()):
            print("Chatbot: Goodbye, Have a wonderful day")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()