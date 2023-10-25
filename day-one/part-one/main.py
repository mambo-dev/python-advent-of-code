def main():
    puzzle_input = read_file_contents("puzzle-input.txt")
    most_calories = find_most_calories(puzzle_input)
    print(most_calories)
    find_most_calories_diff(puzzle_input)


#define function to read file
def read_file_contents(path):
    with open(path) as f:
        return f.read()



#define function to find most calories
#my initial implementation
def find_most_calories(puzzle_input):
    elves_object  = {}
    puzzle_array = puzzle_input.split("\n\n")
    most_calories = 0
    for i in range(0,len(puzzle_array)):
        each_elve = puzzle_array[i].split()
        elves_object[i] = each_elve

    for elves in elves_object:
 
        total = 0
        for elves_load in elves_object[elves]:
            number_elve_load = int(elves_load)
            total+= number_elve_load
            elves_object[elves] = total
            
    most_calories = 0
    for elves in elves_object:
        if elves_object[elves] > most_calories:
            most_calories = elves_object[elves]

    return most_calories

#cleaner way of doing this
def find_most_calories_diff(puzzle_input):
    highest = 0
    totals = 0
    all_elves_load = puzzle_input.strip().split("\n")
    for load in all_elves_load:
        if load == "":
            if totals > highest:
                highest = totals
            totals = 0

        else:
            
            totals += int(load)
    print(highest)
    return highest

main()
