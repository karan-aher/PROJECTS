import re

def analyze_password(password):
    """Evaluate the strength of a password and provide suggestions."""
    strength = 0
    suggestions = []

    # Check length
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Use at least 12 characters for a strong password.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        suggestions.append("Include lowercase letters (a-z).")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        suggestions.append("Include uppercase letters (A-Z).")

    # Check for digits
    if re.search(r'\d', password):
        strength += 1
    else:
        suggestions.append("Include digits (0-9).")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 2
    else:
        suggestions.append("Include special characters (!@#$%^&*(),.?\":{}|<>).")

    # Check for common patterns
    common_patterns = ["password", "123456", "qwerty", "letmein", "abc123"]
    if any(pattern in password.lower() for pattern in common_patterns):
        strength -= 2
        suggestions.append("Avoid common patterns like 'password', '123456', or 'qwerty'.")

    # Ensure no whitespace
    if re.search(r'\s', password):
        strength -= 1
        suggestions.append("Remove spaces or tabs from the password.")

    # Strength rating
    if strength >= 7:
        rating = "Strong"
    elif 4 <= strength < 7:
        rating = "Moderate"
    else:
        rating = "Weak"

    return rating, suggestions


# Main function
def main():
    print("Welcome to the Password Analyzer!")
    password = input("Enter your password to analyze: ")
    rating, suggestions = analyze_password(password)

    print(f"\nPassword Strength: {rating}")
    if suggestions:
        print("Suggestions to improve your password:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("Your password is strong. Great job!")

if __name__ == "__main__":
    main()
