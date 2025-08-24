# make a program in whcih a user will have 10 chances to guess a number between 1 to 100
import random
random_number = random.randint(1,100)

trial = 1
while trial <10:
    guess = int(input(f"{trial} left: You have to 10 chances to guess a number between 1 to 100: "))
    if guess == random_number:
        print(random_number)
        print("You have guessed the right number")
        break
    else:
        if guess>random_number:
            print('ýour number is bigger, please write a smaller number to reach to guess')
        elif guess<random_number:
            print('ýour number is smaller, please write a bigger number to reach to guess')
    trial +=1
         

print('program ended')