def chat_bot():
    # Initialize user data storage
    user_data = {
        'name': None,
        'history': []
    }
    
    # Basic responses dictionary
    responses = {
        'hello': 'Hello! How can I help you today?',
        'hi': 'Hi there! What can I do for you?',
        'bye': 'Goodbye! Have a nice day!',
        'thanks': 'You\'re welcome!',
        'thank you': 'You\'re welcome!',
        'what can you do': 'I can remember your name, perform math operations (+, -, *, /), and chat with you!',
        'help': 'You can ask me to do math, tell me your name, or just chat!'
    }
    
    # Math operations dictionary
    math_ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else 'Error: Division by zero'
    }
    
    print("Welcome to the simple chat bot! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        # Add to conversation history
        user_data['history'].append(f"You: {user_input}")
        
        # Exit condition
        if user_input == 'bye':
            print("Bot:", responses['bye'])
            break
            
        # Check if user is providing their name
        if 'my name is' in user_input:
            name = user_input.replace('my name is', '').strip()
            user_data['name'] = name
            print(f"Bot: Nice to meet you, {name}! I'll remember that.")
            continue
            
        # Check if asking for name
        if 'what is my name' in user_input or 'do you know my name' in user_input:
            if user_data['name']:
                print(f"Bot: Your name is {user_data['name']}!")
            else:
                print("Bot: I don't know your name yet. Tell me your name!")
            continue
            
        # Check for math operations
        math_done = False
        for op in math_ops:
            if op in user_input:
                try:
                    parts = user_input.split(op)
                    num1 = float(parts[0].strip())
                    num2 = float(parts[1].strip())
                    result = math_ops[op](num1, num2)
                    print(f"Bot: The result is {result}")
                    math_done = True
                except (ValueError, IndexError):
                    print("Bot: I couldn't understand that math operation. Please format like '5 + 3'")
                    math_done = True
                break
                
        if math_done:
            continue
            
        # Check stored responses
        response_found = False
        for key in responses:
            if key in user_input:
                print("Bot:", responses[key])
                response_found = True
                break
                
        # Default response if nothing matched
        if not response_found:
            print("Bot: I'm not sure how to respond to that. Can you ask something else?")
            
    # Print conversation history if requested at the end
    if user_data['history']:
        print("\nConversation history:")
        for line in user_data['history']:
            print(line)

# Start the chat bot
chat_bot()