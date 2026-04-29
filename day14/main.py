import random
import art
from game_data import data

print(art.logo)

def play(score,index):

    celebrityA, follower_countA, descriptionA, countryA, indexA = get_celebrity(index)

    print(f"Compare A : {celebrityA}, {descriptionA}, from  {countryA}")
    print(art.vs)
    celebrityB, follower_countB, descriptionB, countryB, indexB = choose_celebrity()

    if indexA == indexB:
        celebrityB, follower_countB, descriptionB, countryB, indexB = choose_celebrity()

    print(f"Against B : {celebrityB}, {descriptionB}, from  {countryB}")

    user_answer = input("Who has more followers? Type 'A' or 'B' : ").lower()
    if user_answer == "a" and follower_countA > follower_countB:
        score += 1
        print (f"You are right! Current Score: {score}")
        return score, True, indexA
    elif user_answer == "b" and follower_countB > follower_countA:
        score += 1
        print (f"You are right! Current Score: {score}")
        return score, True, indexB
    else:
        print(f"Sorry! thats wrong!   Final score is {score}")
        return score, False, indexA


def choose_celebrity():
    length_of_data = len(data)
    random_index = random.randint(1, length_of_data - 1)
    name = data[random_index]["name"]
    follower_count = data[random_index]["follower_count"]
    description = data[random_index]["description"]
    country = data[random_index]["country"]
    return name, follower_count, description, country, random_index

def get_celebrity(index):
    name = data[index]["name"]
    follower_count = data[index]["follower_count"]
    description = data[index]["description"]
    country = data[index]["country"]
    return name, follower_count, description, country,index

continue_playing = True
score = 0
celebrityA, follower_countA, descriptionA, countryA, indexA = choose_celebrity()

while continue_playing:
    score, continue_playing, index_of_previos_round_winner= play(score, indexA)
    indexA = index_of_previos_round_winner
    # celebrityA, follower_countA, descriptionA, countryA, indexA = get_celebrity(indexA)

