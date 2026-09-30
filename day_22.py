import random

print("🎮 Welcome to Number Guessing Game!")
print("I have selected a number between 1 and 100.")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("⚠️ Please enter a number between 1 and 100.")
        
        elif guess < secret_number:
            print("📈 Too low! Try a higher number.")

        elif guess > secret_number:
            print("📉 Too high! Try a lower number.")

        else:
            print("\n🎉 Congratulations!")
            print(f"You guessed the number in {attempts} attempts.")
            break

    except ValueError:
        print("❌ Please enter a valid number.")