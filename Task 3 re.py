import re

def check_password_strength(password):
    # Criteria initialization
    strength_score = 0
    feedback = []

    # 1. Check Length
    if len(password) >= 12:
        strength_score += 2
        feedback.append("Good length (12+ characters).")
    elif len(password) >= 8:
        strength_score += 1
        feedback.append("Minimum length met.")
    else:
        feedback.append("Too short! Use at least 8 characters.")

    # 2. Check Uppercase
    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        feedback.append("Add uppercase letters.")

    # 3. Check Lowercase
    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        feedback.append("Add lowercase letters.")

    # 4. Check Numbers
    if re.search(r'\d', password):
        strength_score += 1
    else:
        feedback.append("Add at least one number.")

    # 5. Check Special Characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>+=-]', password):
        strength_score += 1
    else:
        feedback.append("Add special characters (e.g., @, #, $).")

    # Strength Rating
    if strength_score <= 2:
        rating = "Weak"
    elif strength_score <= 4:
        rating = "Medium"
    else:
        rating = "Strong"

    return rating, feedback

# --- User Interaction ---
user_input = input("Enter a password to test: ")
rating, suggestions = check_password_strength(user_input)

print(f"\nStrength Rating: {rating}")
print("Suggestions/Feedback:")
for note in suggestions:
    print(f"- {note}")