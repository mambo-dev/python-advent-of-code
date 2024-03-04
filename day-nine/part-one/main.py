def main():
    print("=== advent of code day nine ===")
    main_input = read_file_contents("main-input.txt")
    example_input = read_file_contents("example-input.txt")
    start_simulation(example_input)


def start_simulation(input):

    current_positions = {
        "head_position":0,
        "tail_position":0,
        "start_position":0
    }

    for input in input.split("\n"):
        if input[0] == "R":
            move_right(current_positions, int(input[2]))

    #position name start, headPosition , tailPosition if head moves position to 1 then tail is 1 - 1, move to two tail is 2 -1
    pass

def move_right(positions, steps):
    for i in range(0, steps):
        positions["head_position"] += 1
        difference = positions["head_position"] - positions["tail_position"]
        if difference > 1:
            positions["tail_position"] += 1
    
    return positions


def read_file_contents(file_name):
    try:
        with open(file_name) as file:
            return file.read()
    except FileNotFoundError:
        raise Exception("The file you are trying to open was not found")




main()

