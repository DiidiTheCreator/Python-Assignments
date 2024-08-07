
############### Bug list #####################
# Needs play testing, I KNOW there are bugs!
###################################

import random

print('''

▀█████████▄   ▄█          ▄████████  ▄████████    ▄█   ▄█▄      ▄█    ▄████████  ▄████████    ▄█   ▄█▄ 
  ███    ███ ███         ███    ███ ███    ███   ███ ▄███▀     ███   ███    ███ ███    ███   ███ ▄███▀ 
  ███    ███ ███         ███    ███ ███    █▀    ███▐██▀       ███   ███    ███ ███    █▀    ███▐██▀   
 ▄███▄▄▄██▀  ███         ███    ███ ███         ▄█████▀        ███   ███    ███ ███         ▄█████▀    
▀▀███▀▀▀██▄  ███       ▀███████████ ███        ▀▀█████▄        ███ ▀███████████ ███        ▀▀█████▄    
  ███    ██▄ ███         ███    ███ ███    █▄    ███▐██▄       ███   ███    ███ ███    █▄    ███▐██▄   
  ███    ███ ███▌    ▄   ███    ███ ███    ███   ███ ▀███▄     ███   ███    ███ ███    ███   ███ ▀███▄ 
▄█████████▀  █████▄▄██   ███    █▀  ████████▀    ███   ▀█▀ █▄ ▄███   ███    █▀  ████████▀    ███   ▀█▀ 
             ▀                                   ▀         ▀▀▀▀▀▀                            ▀          
''')
print("\nWelcome! Ready to play some Blackjack? Let's begin!\n")
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_over = False

starting_deal = {
    "a": random.choice(deck),
    "b": random.choice(deck),
    "c": random.choice(deck),
    "d": random.choice(deck),
}

# Normal deals for cards
new_card = random.choice(deck)

# All dealt cards for each player (TESTED, WORKS)
user_delt_cards = []
computer_delt_cards = []

# Game starts and four random cards are chosen and assigned (TESTED, WORKS)
user_delt_cards.append(starting_deal["a"])
user_delt_cards.append(starting_deal["b"])
computer_delt_cards.append(starting_deal["c"])
computer_delt_cards.append(starting_deal["d"])

# game enters continuous loop for playing
while game_over is False:

    # Continuous summation of the cards (TESTED, WORKS)
    user_total = 0
    computer_total = 0
    for number in user_delt_cards:
        user_total += number
    for number in computer_delt_cards:
        computer_total += number

    # User is shown their hand (and the total for convenience)
    print(f"User hand: {user_delt_cards}. (Total: {user_total}).")

    if user_total == 21:
        print("You win!")
        break
    if computer_total == 21:
        print(f"Computer's total is {computer_total}!")
        print("You lose!")
        break

    def ace_check():
        global user_total
        if user_total > 21:
            if 11 in user_delt_cards is False:
                print(f"You are not eligible for the ace check.")
                return 0
            if 11 in user_delt_cards:
                print("An 11 was found!")
                for i in user_delt_cards:
                    if i == 11:
                        i = 1
                        a = 11
                        user_delt_cards.remove(a)
                        user_delt_cards.append(i)
                        print(f"Uh oh, you went over 21! Lets swap the ace with a 1: {user_delt_cards}")
                temp_total = 0
                for i in user_delt_cards:
                    temp_total += i
                print(f"The updated total is {temp_total}.")
                user_total = temp_total
                return user_total

    if 0 == ace_check():
        print("You lose the ace check. Game over")
        break

    if user_total < 21 or ace_check() is None:
        continue_choice = input("'Would you like another card dealt to you?' Y/N\n").lower()
        if continue_choice == "y":
            user_delt_cards.append(random.choice(range(2, 12)))
            user_total = 0
            for number in user_delt_cards:
                user_total += number
            ace_check()
            if user_total > 21:
                print(f"Computer hand: {computer_delt_cards}.")
                print(f"With your new card, your total is {user_total}. You lose!")
                break

        if continue_choice == "n":
            print("You no longer want cards! Let's see how this ends.")

            while computer_total < 17:  # computer draws card if under 17 (repeatable)
                computer_delt_cards.append(new_card)
                print("Computer drew a card!")
                computer_total = 0
                for i in computer_delt_cards:
                    computer_total += i
                print(f"Computer hand: {computer_delt_cards}\nNew computer total for now is {computer_total}.")
                if computer_total > 21:
                    if 11 in computer_delt_cards is False:
                        print(f"Computer is STILL not eligible for the ace check. You win!")
                        break
                    if 11 in computer_delt_cards:
                        print("An 11 was found!")
                        for i in computer_delt_cards:
                            if i == 11:
                                i = 1
                                a = 11
                                computer_delt_cards.remove(a)
                                print(f"We removed the 11: {computer_delt_cards}")
                                computer_delt_cards.append(i)
                                print(f"We swapped it with a 1: {computer_delt_cards}")
                        temp_total = 0
                        for i in computer_delt_cards:
                            temp_total += i
                        print(f"The temp total for computer is {temp_total}.")
                        computer_total = temp_total
            if 17 <= computer_total < 21:
                if user_total < computer_total:
                    print(f"Your cards add up to {user_total}, and computer's adds up to {computer_total}. You lose!")
                    break
                elif user_total > computer_total:
                    print(f"Your cards add up to {user_total}, and computer's adds up to {computer_total}. You win!")
                    break
                elif user_total == computer_total:
                    print(f"Your cards add up to {user_total}, and computer's adds up to {computer_total}. DRAW!")
                    break
