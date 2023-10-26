import string
import functools


def main():
    print("=== advent of code day 3 ===")
    example_file_content = read_file_contents("example-input.txt")
    main_file_content = read_file_contents("main-input.txt")
    rucksack(main_file_content)
    print(define_group_rucksack(main_file_content))


def rucksack(file_contents):
    prioritized_letters = return_letter_priority()
    rucksacks = file_contents.split("\n")
    common_letters = []
    for sack in rucksacks:
        common_letters.append(find_common_letter(sack, prioritized_letters))

    return functools.reduce(lambda a, b: a + b, common_letters)


def define_group_rucksack(file_contents):
    rucksacks = file_contents.split("\n")
    group_rucksack = {}
    # every group split in three
    for i in range(0, len(rucksacks), 3):
        group_rucksack[i] = rucksacks[i:i+3]
    common_in_the_three_groups = []
    for rucksack in group_rucksack:
        common_in_the_three_groups.append(
            find_common_in_group(group_rucksack[rucksack]))

    prioritized_letters = return_letter_priority()
    common_items_priority = []
    for common in common_in_the_three_groups:
        common_items_priority.append(prioritized_letters[common])

    return functools.reduce(lambda a, b: a + b, common_items_priority)


def find_common_in_group(group_sack):
    first_ruck_sack = group_sack[0]
    second_ruck_sack = group_sack[1]
    third_ruck_sack = group_sack[2]
    for first in first_ruck_sack:
        if first in second_ruck_sack and first in third_ruck_sack:
            return first


def find_common_letter(line, prioritized_letters):

    first_half = line[0:int(len(line) / 2)]
    second_half = line[int(len(line) / 2):]

    for first in first_half:
        if first in second_half:

            return prioritized_letters[first]


def return_letter_priority():
    letters = []
    for lower_letter in string.ascii_lowercase:
        letters.append(lower_letter)
    for upper_letter in string.ascii_uppercase:
        letters.append(upper_letter)

    prioritized_letters = {}
    for i in range(0, len(letters)):
        prioritized_letters[letters[i]] = i + 1

    return prioritized_letters


def read_file_contents(filename):
    with open(filename) as file:
        return file.read()


main()
