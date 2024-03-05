def main():
    print("=== advent of code day nine ===")
    main_input = read_file_contents("main-input.txt")
    example_input = read_file_contents("example-input.txt")
    start_simulation(example_input)


def start_simulation(input):
    visited = 0

    current_positions = {
        "head_positions":{
            "U":0,
            "R":0,
            "D":0,
            "L":0
        },
        "tail_positions":{
            "U":0,
            "R":0,
            "D":0,
            "L":0
        },
        "start_position":0
    }

    for input in input.split("\n"):
        steps = int(input[2])
        direction = input[0]
        
        if direction == "R":
           current_positions, visited = move_right(current_positions, steps , visited)
           print(visited)

        if direction == "U":
            current_positions, visited = move_up(current_positions, steps, visited)
            print(visited)
    
    print(current_positions, visited)

    #position name start, headPosition , tailPosition if head moves position to 1 then tail is 1 - 1, move to two tail is 2 -1
    pass

def move_right(positions, steps, visited):
    for i in range(0, steps):
        positions["head_positions"]["R"] += 1
        difference = positions["head_positions"]["R"] - positions["tail_positions"]["R"]
        if difference > 1:
            visited += 1 
            positions["tail_positions"]["R"] += 1
    
    return positions, visited

def move_up(positions, steps, visited):
    for i in range(0, steps):
        if positions["head_positions"]["U"] == 0:
            positions["head_positions"]["L"] += 1
        positions["head_positions"]["U"] += 1
        
        difference = positions["head_positions"]["U"] - positions["tail_positions"]["U"]

        if difference > 1:
            visited += 1 
            positions["tail_positions"]["U"] += 1
    
    return positions, visited




def read_file_contents(file_name):
    try:
        with open(file_name) as file:
            return file.read()
    except FileNotFoundError:
        raise Exception("The file you are trying to open was not found")




main()

