import random
import sys

print("Welcome to RPS!")
moves: dict = {"rock": "🪨", "paper": "📃", "scissors": "✂️"}
valid_moves: list[str] = list(moves.keys())
user_count = 0
ai_count = 0

while True:
    user_move: str = input("Rock, paper or scissors? >>> ").lower()

    if user_move == "exit":
        print("Thanks for playing!")
        sys.exit()
    if user_move not in valid_moves:
        print("Invalid move...")
        continue

    ai_move: str = random.choice(valid_moves)

    print("-----")
    print(f"You: {moves[user_move]}")
    print(f"AI: {moves[ai_move]}")
    print("-----")

    if user_move == ai_move:
        print("It is a tie!")
    elif user_move == "rock" and ai_move == "scissors":
        user_count += 1
        print("You win!")
    elif user_move == "scissors" and ai_move == "paper":
        user_count += 1
        print("You win!")
    elif user_move == "paper" and ai_move == "rock":
        user_count += 1
        print("You win!")
    else:
        ai_count += 1
        print("AI wins!")
    print(f"Score: You {user_count} - AI {ai_count}")
