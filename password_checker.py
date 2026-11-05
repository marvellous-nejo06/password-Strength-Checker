# Password Strength Checker
# Created by Marvellous Dele Nejo - Aspiring Cybersecurity Analyst

def check_password(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 2
    else:
        feedback.append("Password too short. Use at least 8 characters.")

    # Check for uppercase
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add an UPPERCASE letter (A-Z).")

    # Check for lowercase
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add a lowercase letter (a-z).")

    # Check for numbers
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add a number (0-9).")

    # Check for symbols
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if any(c in symbols for c in password):
        score += 1
    else:
        feedback.append("Add a symbol like ! @ # $.")

    # Show result
    print("\n--- RESULT ---")
    print(f"Password Score: {score}/6")

    if score == 6:
        print("STRONG - Great password!")
    elif score >= 4:
        print("MEDIUM - Good, but can be better.")
    else:
        print("WEAK - Hackers can guess this easily!")

    for tip in feedback:
        print(tip)

# Ask user for password
my_password = input("Enter a password to check: ")
check_password(my_password)
