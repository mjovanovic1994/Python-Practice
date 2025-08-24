import random
 # make below code a function so you just call a function to get reuslt    
def rps(user:str):
    """"this function takesre user and return the """
    comp = random.choice(['rock','scissors','paper'])
    print(f"Computer chose: {comp}")
    if user == comp:
        return "Draw" 
    elif (user == "rock" and comp == "scissors") or \
        (user == "scissors" and comp == "paper") or \
        (user == "paper" and comp == "rock"):
        return "You win"

        
    elif (comp == "rock" and user == "scissors") or \
        (comp == "scissors" and user == "paper") or \
        (comp == "paper" and user == "rock"):
        return "You lose"
    else:
        print(f"invalid please choose between 'rock','scissors','paper'")
        return "ïnvalid"
        
    
