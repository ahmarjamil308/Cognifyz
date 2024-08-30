def evaluate_password_strength(password):
    # Check criteria
    length_ok = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+{}:\"<>?~" for c in password)

    # Determine strength
    if length_ok and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif length_ok and (has_upper or has_lower) and has_digit:
        return "Moderate"
    else:
        return "Weak"

# Example usage
password = input("Enter a password to evaluate: ")
strength = evaluate_password_strength(password)
print(f"Password strength: {strength}")
