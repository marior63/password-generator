import random
import string

#this version excludes {} and []

def generate_strong_password(length=12):
    # Define the character sets for the password
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits

    # Exclude brackets and braces from special characters
    special_characters = '!@#$%^&*()_-+=<>?/|'

    # Combine all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure at least one character from each set is included in the password
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the remaining length with random characters
    password.extend(random.choice(all_characters) for _ in range(length - 4))

    # Shuffle the password characters
    random.shuffle(password)

    # Convert the list of characters to a string
    final_password = ''.join(password)

    return final_password

# Set your desired password length (default is 12 characters)
password_length = 16

# Generate a strong password
strong_password = generate_strong_password(password_length)

# Print the generated password
print("Generated Strong Password:", strong_password)
