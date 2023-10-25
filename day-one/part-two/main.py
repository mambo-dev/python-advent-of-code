import functools


def main():
    file_contents = read_file_contents("puzzle-input.txt")
    smaller_puzzle_file_contents = read_file_contents(
        "smaller-puzzle-input.txt")

    top_three_elves = []

    for i in range(0, 3):
        highest, file_contents = find_and_remove_highest(file_contents)
        top_three_elves.append(highest)

    total_carried_by_all = functools.reduce(lambda a, b: a+b, top_three_elves)

    print("the top three elves are carrying", total_carried_by_all)


def find_and_remove_highest(file_contents):
    all_elves_load = file_contents.strip().split("\n\n")
    each_elve_and_total = {}
    for i in range(0, len(all_elves_load)):
        each_elve_and_total[i] = functools.reduce(
            lambda a, b: a + b, map(lambda a: int(a), all_elves_load[i].split("\n")))

    # find highest position index
    highest_elve_position = 0
    for each_elve_total in each_elve_and_total:

        if each_elve_and_total[each_elve_total] > each_elve_and_total[highest_elve_position]:

            highest_elve_position = each_elve_total

    # pop this position out from the list and return its positon
    all_elves_load.remove(all_elves_load[highest_elve_position])

    return each_elve_and_total[highest_elve_position], "\n\n".join(all_elves_load)


def read_file_contents(path):

    with open(path) as f:
        return f.read()


main()
