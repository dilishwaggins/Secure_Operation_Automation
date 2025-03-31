import re
import bcrypt

def check_password_strength(password):
    suggestions = []
    
    if len(password) < 12:
        suggestions.append("Make the password at least 12 characters long.")
    if not any(char.isdigit() for char in password):
        suggestions.append("Include at least one number.")
    if not any(char.isupper() for char in password):
        suggestions.append("Include at least one uppercase letter.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # Fixed regex
        suggestions.append("Include at least one special character (!@#$%^&* etc.).")
    
    if suggestions:
        return False, suggestions
    return True, ["Password is strong!"]

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password.decode()

def run():
    password = input("Enter a password to check: ")
    strong, feedback = check_password_strength(password)
    
    print("\nPassword Strength Feedback:")
    for tip in feedback:
        print(f"- {tip}")
    
    if strong:
        hash_option = input("Do you want to hash this password? (y/n): ").strip().lower()
        if hash_option == 'y':
            print("\nHashed Password:", hash_password(password))

if __name__ == "__main__":
    run()
