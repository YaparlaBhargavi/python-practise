import random 
player1 = input("Select Rock, Paper, or Scissor :").lower()
player2 = input(" select Rock, Paper, Scissor :").lower()
print("Player 2 selected: ", player2)
print("player 1 selected: ", player1)

if player1 == "rock" and player2 == "paper":
    print("Player 2 Won")
elif player1 == "paper" and player2 == "scissor":
    print("Player 2 Won")
elif player1 == "scissor" and player2 == "rock":
    print("Player 2 Won")
elif player1 == player2:
    print("Tie")
else:
    print("Player 1 Won")