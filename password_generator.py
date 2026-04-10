import secrets
import string


def generate_strong_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        
        # Validation criteria
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)
        
        if has_upper and has_lower and has_digit and has_special:
            return password

def main():
    print("--- Python Secure Password Generator ---")
    
    try:
        user_length = int(input("Enter desired password length (minimum 8): "))
        
        if user_length < 8:
            print("Length is too short for a strong password. Defaulting to 12.")
            user_length = 12
            
        new_password = generate_strong_password(user_length)
        
        print("\n" + "="*30)
        print(f"Your Password: {new_password}")
        print("="*30)
        
    except ValueError:
        print("Invalid input. Please enter a whole number (e.g., 16).")

if __name__ == "__main__":
    main()
