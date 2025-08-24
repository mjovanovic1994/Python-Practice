# Import random
# Ask the user to enter rock paper or scissors for user
# Randomly choose paper rock or scissors for computer
# If computer == paper print we draw
# If user == “paper” and computer == “rock” print user worn
# End 
# Optional: if you want to make it a function that takes user_input and return you who won then we can do at the 
import random
from rps import rps

options = ["rock", "paper", "scissors"]
results = []
chances = 10
for i in range(chances):
    user = input(f"plesae choose {options}")
    result = rps(user)
    print(result)
    results.append(result)
print("results are {results}")

        
            
      