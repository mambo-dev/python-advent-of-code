def main():
    print("=== advent of code day five ===")
    main_input = read_file_contents("main-input.txt")
    example_input = read_file_contents("example-input.txt")
    crates, instructions = split_crates_and_instructions(example_input)
    final_result = execute_instructions(instructions, crates)
    print(final_result)

#split the instructions and crates into two pieces i can use
def split_crates_and_instructions(file_contents):
 
    split_contents = file_contents.split("\n\n")
    crates = split_contents[0]
    instructions = split_contents[1]
    crates_dict = {}

    return transform_crates(crates), transform_instructions(instructions)

def transform_crates(crates):
    
    crate_lines = crates.split("\n")
    base_dict = {}
    remaining_lines = []
    value_positions  = []
    for lines in crate_lines:
        for i in range(0, len(lines)):
            if lines[i] != " " and lines[i] != "[" and lines[i] != "]":
                base_dict[i] = []
                value_positions.append((lines[i], i))
     
   
    for value in value_positions:
        for dict_values in base_dict:
            if value[1] == dict_values:
                base_dict[dict_values].append(value[0])

    return base_dict

        

        

# return instructions in array of tuples move from to 
def transform_instructions(instructions):
    
    separate_instructions = instructions.split("\n")
    all_instructions = []
    for instruction in separate_instructions:
        stripped_instructions = []
        for single_instructions in instruction:
            if single_instructions.isnumeric():
                stripped_instructions.append(single_instructions)
        all_instructions.append(tuple(map(lambda a: int(a), stripped_instructions)))
        
    return all_instructions


def execute_instructions(instructions,  crates):
    
    for instruction in instructions:
        print(instruction)

    return ""

def read_file_contents(file_name):
    with open(file_name) as file:
        return file.read()

main()