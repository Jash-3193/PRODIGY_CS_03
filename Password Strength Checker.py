import re
def check_password_strength(password):
    # Initialize the strength score
    strength = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for upper case letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lower case letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters
    if re.search(r'[@#$%^&+=]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Assess overall strength
    if strength == 5:
        feedback.append("Password is very strong.")
    elif strength == 4:
        feedback.append("Password is strong.")
    elif strength == 3:
        feedback.append("Password is moderate.")
    else:
        feedback.append("Password is weak.")

    return feedback

password = input("Enter your password: ")
strength_feedback = check_password_strength(password)
for line in strength_feedback:
    print(line)
