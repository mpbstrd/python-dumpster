import random

def rps():
    rps = ['rock','paper','scissors']

    bot_choice = random.choice(rps)
    player_choice = input("Pick: ")
    if player_choice == bot_choice:
        print('You win :D \n You picked: {} \n Bot picked: {}'.format(player_choice,bot_choice))
    else:
        print('You lose :( \n You picked: {} \n Bot picked: {}'.format(player_choice,bot_choice))

def guessing_game():
    random_number = random.randint(1,100)
    print(random_number)
    player_pick = int(input("Pick a number: "))
    for attempts in range(5):
        if random_number == player_pick:
            print("You got the right number in: {} attempt(s)".format(int(attempts+1)))
            break
        elif random_number > player_pick:
            print("The number you are looking for is greater than {}".format(player_pick))
            player_pick = int(input("Try again: "))
        elif random_number < player_pick:
            print("The number you are looking for is less than {}".format(player_pick))
            player_pick = int(input("Try again: "))
        else:
            print("Please enter a number between 1-100 only")
            player_pick = int(input("Try again: "))

