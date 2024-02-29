def main():
    print("=== advent of code day nine ===")
    main_input = read_file_contents("main-input.txt")
    example_input = read_file_contents("example-input.txt")
    start_simulation(main_input)


def start_simulation(input):
    highest_numbers = {
        "R":0,
        "D":0,
        "U":0,
        "L":0
        }

    input_by_line = input.split("\n")
    for input in input_by_line:
        input_by_space = input.split(" ")
        if input_by_space[0] == "R":
            if int(input_by_space[1]) > highest_numbers["R"]:
                highest_numbers["R"] = int(input_by_space[1])

        elif input_by_space[0] == "D": 
            if int(input_by_space[1]) > highest_numbers["D"]:
                highest_numbers["D"] = int(input_by_space[1])

        elif input_by_space[0] == "U": 
            if int(input_by_space[1]) > highest_numbers["U"]:
                highest_numbers["U"] = int(input_by_space[1])

        elif input_by_space[0] == "L": 
            if int(input_by_space[1]) > highest_numbers["L"]:
                highest_numbers["L"] = int(input_by_space[1])

    print(highest_numbers)


def read_file_contents(file_name):
    try:
        with open(file_name) as file:
            return file.read()
    except FileNotFoundError:
        raise Exception("The file you are trying to open was not found")




main()

