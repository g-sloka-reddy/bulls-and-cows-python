import random
def generate_secret_code():
    digits = list('0123456789')
    random.shuffle(digits)
    secret = "".join(digits[:4])
    return secret
def get_bulls_and_cows(secret, guess):
    bulls = 0
    cows = 0

    for i in range(4):
        if secret[i] == guess[i]:
            bulls += 1

    common_digits = len(set(secret) & set(guess))
    cows = common_digits - bulls

    return bulls, cows
def play_game():
    secret_code = generate_secret_code()
    attempts = 0

    print("🐄Welcome to Bulls and Cows!")
    print("I have generated a secret 4-digit number.")
    print("All digits are unique (e.g., 1482, not 1148).")
    print("Try to guess it!")
    print("-" * 30)
    while True:
        guess = input("Enter your 4-digit guess (or 'quit'): ")

        if guess.lower() == 'quit':
            print(f"\nGame quit. The secret number was: **{secret_code}**")
            break

        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter exactly 4 digits.")
            continue

        if len(set(guess)) != 4:
            print("Invalid input. The digits must be unique.")
            continue

        attempts += 1

        bulls, cows = get_bulls_and_cows(secret_code, guess)

        if bulls == 4:
            print(f"\n🎉**CONGRATULATIONS!**🎉")
            print(f"You guessed the number **{secret_code}** in **{attempts}** attempts!")
            break
        else:
            print(f"Hint: {bulls} Bull(s), {cows} Cow(s)")
            print("-" * 30)
if __name__ == "__main__":
    play_game()
