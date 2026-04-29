# Blackjack
import art
import random
print(art.logo)

deck_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]


def choose_card():
    user_card = []
    computer_card = []
    # choosing user card
    user_card.append(random.choice(deck_list))
    user_card.append(random.choice(deck_list))

    # choosing computer card
    computer_card.append(random.choice(deck_list))
    computer_card.append(random.choice(deck_list))

    return user_card, computer_card


def draw_card():
    drawn_card = random.choice(deck_list)
    return drawn_card

def winner_decide(user_cards, computer_cards):

    if sum(user_cards) > 21 and sum(computer_cards) < 21:
        print(f"Computer cards: {computer_cards} Computer's Current Score: {sum(computer_cards)}")
        print(f"Your cards: {user_cards} Computer cards: {computer_cards}")
        print("You went over 21! You lose!")
    elif sum(user_cards) == 21:
        print(f"Computer cards: {computer_cards} Current Score: {sum(computer_cards)}")
        print(f"Your cards: {user_cards} Computer's Computer cards: {computer_cards}")
        print("You got Blackjack! You win!")
    elif sum(computer_cards)== 21 and sum(user_cards) == 21:
        print(f"Computer cards: {computer_cards} Current Score: {sum(computer_cards)}")
        print(f"Your cards: {user_cards} Computer's Computer cards: {computer_cards}")
        print("You both got Blackjack! It's a tie!")
    elif sum(computer_cards) > 21 and sum(user_cards)> 21:
        print(f"Computer cards: {computer_cards} Current Score: {sum(computer_cards)}")
        print(f"Your cards: {user_cards} Computer's Computer cards: {computer_cards}")
        print("You both went over 21! It's a tie!")
    elif sum(computer_cards) < sum(user_cards) <= 21:
        print(f"Computer cards: {computer_cards} Current Score: {sum(computer_cards)}")
        print(f"Your cards: {user_cards}  Computer's Computer cards: {computer_cards}")
        print("You win!")
    elif sum(user_cards) < sum(computer_cards) <= 21:
        print(f"Computer cards: {computer_cards} Current Score: {sum(computer_cards)}")
        print(f"Your cards: {user_cards} Computer's Computer cards: {computer_cards}")
        print("You lose!")
    elif sum(user_cards) == sum(computer_cards):
        print("It's a draw!")

def check_cards(cards):
    while sum(cards) > 21 and 11 in cards:
        cards[cards.index(11)] = 1
    return cards


def computer_draw_card_or_not(card_list):
    if sum(card_list) <= 16:
        card_list.append(draw_card())
        check_cards(card_list)
    return card_list



user_input = input("Welcome to Blackjack! Press ENTER to begin. y or n: ")
if user_input == "y":
    game_continue = True

while game_continue:
    user_cards, computer_cards = choose_card()
    print(f"Your cards: {user_cards} Current Score: {sum(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

    get_card_or_not = input("type y to get another card or n to pass: ")

    while get_card_or_not == "y":
        user_cards.append(draw_card())
        check_cards(user_cards)
        print(f"Your cards: {user_cards} Your Current Score: {sum(user_cards)}")

        if sum(user_cards) > 21:
            break

        get_card_or_not = input("type y to get another card or n to pass: ")

    computer_cards = computer_draw_card_or_not(computer_cards)
    winner_decide(user_cards, computer_cards)


    x = input("Do you want to play again? y or n:")
    if x == "n":
        game_continue = False









