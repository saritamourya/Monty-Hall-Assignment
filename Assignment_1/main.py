##Import a library file
import random
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

## Creating a funtion to define the door without the prize
def no_prize_door(host, no_of_doors, choices_of_players):
    a = 1
    while a == choices_of_players or a == host:
        a = (a + 1) % no_of_doors
    return a

##Creating a funtion to define the switching procedure from one door to another
def switch_fun(displayed_door, no_of_doors, choices_of_players):
    a = 1
    while a == choices_of_players or a == displayed_door:
        a = (a + 1) % no_of_doors
    return a

##Creating a funtion for the Monty hall Simulation
def game(switch, no_of_tests):
    win_switch_count = 0
    lose_switch_count = 0
    doors = ['goat', 'goat', 'car'] ## Creating a list with three element which consists of one door with car and other
    ##two with the goats.
    no_of_doors = len(doors) # Assigning the length of the list in the variable.
    for a in range(0, no_of_tests): ## Creating a loop for number of times the game will be played
        prize_door = random.randint(0, no_of_doors - 1) ## door with the prize is shuffled and assigned.
        host = prize_door ## Host knows the door with the car.
        choices_of_players = random.randint(0, no_of_doors - 1) ## Player selected the door randomly
        players_original_choice = choices_of_players
        displayed_door = no_prize_door(host, no_of_doors, choices_of_players)##
        if switch == True: ## Stating condition to keep on switching from one door to another
            choices_of_players = switch_fun(displayed_door, no_of_doors, choices_of_players)
        if choices_of_players == prize_door:
            win_switch_count += 1 ## Increment in the number of the wins the player obtains.
            print("Winner-the player chose door with the car=", choices_of_players, 'players_original_choice=',
                  players_original_choice, 'prize door=', prize_door, 'displayed door=', displayed_door)
        elif choices_of_players != prize_door:
            lose_switch_count += 1 ##Increment in the number of loss counts as the player lose the game.
            print('Lost-the player chose door with the goat=', choices_of_players, 'players_original_choice=',
                  players_original_choice, 'prize door=', prize_door, 'displayed door=', displayed_door)
        else:
            print('SOMETHING WENT WRONG')
            ## Calculating the percentage of the win and loss
    print('win percentage:', (win_switch_count / no_of_tests) * 100, 'lose percentage:',
          (lose_switch_count / no_of_tests) * 100, 'no of tests', no_of_tests)


game(True, 1000)
