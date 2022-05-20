import random

def rps():
    rps = ['rock','paper','scissors']

    bot_choice = random.choice(rps)
    player_choice = input("\n Pick: ")
    if player_choice == bot_choice:
        print('You win :D \n You picked: {} \n Bot picked: {}'.format(player_choice,bot_choice))
    else:
        print('You lose :( \n You picked: {} \n Bot picked: {}'.format(player_choice,bot_choice))

def guessing_game():
    random_number = random.randint(1,100)
    print(random_number)
    
    attempts = 1
    while attempts <= 5:
        player_pick = int(input("Pick a number: "))
        if random_number == player_pick:
            print("You got the right number in: {} attempt(s)".format(int(attempts)))
            break
        elif random_number > player_pick:
            print("The number you are looking for is greater than {}".format(player_pick))
        elif random_number < player_pick:
            print("The number you are looking for is less than {}".format(player_pick))
        else:
            print("Please enter a number between 1-100 only")
        if attempts == 5:
                print("You already reached the maximum guesses. Better luck next time!")
                break
        attempts += 1

print("Enter 1 for rock, paper and scissors.")
print("Enter 2 for guessing game.")
player = int(input("What game shall we play? "))
if player == 1:
    rps()
elif player == 2:
    guessing_game()
else:
    print("Please choose a valid number.")