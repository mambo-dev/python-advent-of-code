import string
import functools

def main():
    print("=== advent of code day 3 ===")
    example_file_content = read_file_contents("example-input.txt")
    main_file_content = read_file_contents("main-input.txt")
    print(rucksack(main_file_content))


def rucksack(file_contents):
    prioritized_letters = return_letter_priority()
    rucksacks = file_contents.split("\n")
    common_letters = []
    for sack in rucksacks:
        common_letters.append(find_common_letter(sack,prioritized_letters))
    
    return functools.reduce(lambda a,b: a + b, common_letters)
        

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