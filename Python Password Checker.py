def check_password_strength(password):
    # Rule 1: Minimum length
    has_length = len(password) >= 8

    # Rule 2: Contains uppercase letter
    has_upper = any(char.isupper() for char in password)

    # Rule 3: Contains a number/digit
    has_digit = any(char.isdigit() for char in password)

    # Rule 4: Contains a special symbol
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
    has_symbol = any(char in symbols for char in password)

    # Count how many rules passed
    score = sum([has_length, has_upper, has_digit, has_symbol])

    # A. Password Tips based on what's missing
    tips = []
    if not has_upper:
        tips.append("- Add uppercase letters (e.g. A, B, C)")
    if not has_digit:
        tips.append("- Add numbers (e.g. 1, 2, 3)")
    if not has_symbol:
        tips.append("- Add symbols (e.g. !, @, #)")
    if not has_length:
        tips.append("- Make it at least 8 characters long")

    # Determine strength based on score
    if score <= 1:
        strength = "WEAK ❌ - Your password is very easy to crack!"
    elif score <= 3:
        strength = "MEDIUM ⚠️  - Your password is okay but can be stronger."
    else:
        strength = "STRONG ✅ - Your password is secure!"

    return strength, tips


# --- Main Program ---
print("=== Ejikeme_Ilo Password Strength Checker ===")

# C. Loop so user can retry
while True:
    password = input("\nEnter your password (or type 'quit' to exit): ")

    # Exit option
    if password.lower() == 'quit':
        print("Goodbye! Stay secure. 🔐")
        break

    # B. Prevent very short passwords
    if len(password) < 5:
        print("⚠️  Password too short! Please enter at least 5 characters.")
        continue

    # Run the checker
    result, tips = check_password_strength(password)
    print(f"\nStrength: {result}")

    # Show tips only if password isn't strong
    if tips:
        print("\n💡 Tips to improve your password:")
        for tip in tips:
            print(tip)
    else:
        print("\n🎉 Great job! No improvements needed.")