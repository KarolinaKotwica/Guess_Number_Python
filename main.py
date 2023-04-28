import random

def start():
    print("\nWelcome to the number Guessing game")
    print("Guess the number from 1 to 100")
    difficulty = input("Choose the difficulty: Type 'easy' or 'hard': ")
    
    attempt = 5
    if difficulty == 'easy':
        attempt = 10
    
    randomNumber = random.randint(0, 100)
    answer = ''
    
    while attempt != 0:
        print(f"\nYou have {attempt} attempts remaining to guess the number")
        answer = int(input("Make a guess: "))
        if answer == randomNumber:
            print(f"Bravo! The number was {randomNumber}!")
            break
        elif answer > randomNumber:
            print("too high")
        else:
            print("to low")
            
        attempt = attempt - 1
        
    if attempt == 0:
        print(f"\nGame over. If you want you can play again :)\nThe number was {randomNumber}")
        
    playAgain = input('Do you want to play again? Y / N ')
    
    if playAgain == 'Y':
        start()
        
start()