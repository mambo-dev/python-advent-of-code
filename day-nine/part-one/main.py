import functools

def main():
    print("=== advent of code day nine ===")
    main_input = read_file_contents("main-input.txt")
    example_input = read_file_contents("example-input.txt")
    start_simulation(example_input)


def start_simulation(input):
    visited = 0
    highest_positions = {
        "left":0,
        "right":0,
        "up":0,
        "down":0
    }
    movements = input.split("\n")

    for input in movements:
        step = int(input[2])
        match input[0]:
            case "L":
                if(highest_positions["left"] < step):
                    highest_positions["left"] = step
            case "R":
                if(highest_positions["right"] < step):
                    highest_positions["right"] = step
            case "U":
                if(highest_positions["up"] < step):
                    highest_positions["up"] = step
            case "D":
                if(highest_positions["down"] < step):
                    highest_positions["down"] = step
            case _:
                print("something went wrong")
            
    columns = highest_positions["left"] + highest_positions["right"]
    rows = highest_positions["up"] + highest_positions["down"]
    knot_positions = [[{"visited":False}]*columns ] * rows
    for i in range(0, len(movements) - 1):
        steps = movements[i][2]
        direction = movements[i][0]
        for step in range(1, int(steps) + 1):
         
            if(direction == "R"):
                knot_positions[len(knot_positions) - 1][step] = {"visited":True}
            elif(direction == "U"):
                knot_positions[len(knot_positions) -1][step]= {"visited":True}

    print(knot_positions)
           
            

    # sposition name start, headPosition , tailPosition if head moves position to 1 then tail is 1 - 1, move to two tail is 2 -1
    pass


def pull_tail(steps, direction, positions):
    visited = 0
    saveVisits = []
    for i in range(0, steps):
        difference = positions["head_positions"][direction] - positions["tail_positions"][direction]
        head_position = positions["head_positions"][direction]
        if(difference > 0):
            positions["tail_positions"][direction] = head_position
            visited += 1
            

        positions["head_positions"][direction] += 1


    print(visited, saveVisits)
    return visited





def read_file_contents(file_name):
    try:
        with open(file_name) as file:
            return file.read()
    except FileNotFoundError:
        raise Exception("The file you are trying to open was not found")




main()

