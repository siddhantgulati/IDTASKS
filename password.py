import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    # Define character sets based on user's choices
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    # Check if at least one character set is selected
    if not characters:
        return "Error: Please select at least one character set."

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")

    # Get user preferences
    length = int(input("Enter the length of the password: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"
    use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

    # Generate and display the password
    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)
    print("Your generated password is:", password)

if __name__ == "__main__":
    main()
