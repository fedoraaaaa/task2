import random

def generate_secure_password(length):
    # Define character sets
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    
    # Combine all characters
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    
    # Ensure the password includes at least one character from each set
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    # Fill the rest of the password length with random characters from all sets
    for _ in range(length - 4):
        password.append(random.choice(all_characters))
    
    # Shuffle the list to avoid predictable patterns
    random.shuffle(password)
    
    # Convert the list to a string
    return ''.join(password)

# Get user input for password length
try:
    length = int(input("Enter the desired password length (minimum 4): "))
    if length < 4:
        print("Password length must be at least 4. Setting length to 4.")
        length = 4
except ValueError:
    print("Invalid input. Setting password length to default (12).")
    length = 12

# Generate and print the password
password = generate_secure_password(length)
print("Generated Password:", password)