import functools


def main():
    print("=== yeeei day two ===")
    example_input = read_file_contents("example-input.txt")
    main_input = read_file_contents("main-input.txt")
    print("=== the results for this challenge are ===")
    print(calculate_total_score(main_input))


def calculate_total_score(input):
    list_with_all = []
    scores = input.split("\n")
    all_rounds = {}
    # go through the input and set each round with your  choice and opponents choice in a dictionary of tuples
    for i in range(0, len(scores)):
        opponent_pick = scores[i].split()[0]
        my_pick = scores[i].split()[1]
        all_rounds[i] = (opponent_pick, my_pick)

    score = []
    # go through each round appending the score returned from the find round score function
    for round in all_rounds:
        score.append(find_round_score(all_rounds[round]))

    return functools.reduce(lambda sum, b: sum + b, score)


def find_round_score(round):
    choices = {
        "rock": "A",
        "paper": "B",
        "scissors": "C",
    }
    opponent_pick = return_choice_option(round[0], choices)
    my_pick = evaluate_my_choice(opponent_pick, round[1])

    # if my pick beats opponent pick find my score and return it

    return find_fight_result(opponent_pick, my_pick)


# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
# evaluate and return choice i make based on guide
def evaluate_my_choice(opponent_pick, guide):

    # draw
    if guide == "Y":
        return opponent_pick
    # win
    elif guide == "Z":

        return "paper" if opponent_pick == "rock" else "rock" if opponent_pick == "scissors" else "scissors"
    # loss
    else:

        return "rock" if opponent_pick == "paper" else "paper" if opponent_pick == "scissors" else "scissors"


def return_choice_option(persons_pick, choices):
    for choice in choices:
        if persons_pick == choices[choice]:
            return choice


def find_fight_result(opponent_pick, my_pick):
    score = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
    }
    # draw
    if opponent_pick == my_pick:

        return score[my_pick] + 3
    # win
    elif (opponent_pick == "rock" and my_pick == "paper") or (opponent_pick == "paper" and my_pick == "scissors") or (opponent_pick == "scissors" and my_pick == "rock"):

        return score[my_pick] + 6
    # loss
    else:

        return score[my_pick]


def read_file_contents(file_name):
    with open(file_name) as file:
        return file.read()


main()
