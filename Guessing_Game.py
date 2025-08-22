import random

easy_words = ["apple","train","tiger","money","india"]
medium_words = ["python","bottle","monkey","planet","laptop"]
hard_words = ["elephant","umbrella","diamond","computer","mountain"]

print("\nWelcome to the Password Guessing Game")
print("Choose a Difficulty Level: easy, medium, hard")

level = input("Enter a Difficulty Level:").lower()

if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice. Defaulting to Easy level;")
    secret = random.choice(easy_words)

attempts = 0
print("\nGuess the secret Password")

# Game Loop >> 
while True:
    guess = input("Enter your guess :").lower()
    attempts += 1
    if guess == secret:
        print(f"Congrats You Win, No. Of attempts {attempts}")
        break

    hint =""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:  # compare each word of secret with guess word
            hint += guess[i]  # if mattched so store in hint with guess word
        else:
            hint += "_"
    
    print("Hint: ",hint)
print("Game Over!")
