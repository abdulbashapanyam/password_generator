import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Define character sets based on user preferences
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    digit_chars = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''
    
    # Combine all selected characters
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars
    
    # Ensure that at least one character type is chosen
    if not all_chars:
        raise ValueError("At least one character type must be selected!")
    
    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 1): "))
            if length < 1:
                print("Length must be at least 1.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")
    
    # Get user preferences for password complexity
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
    # Generate and display the password
    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
