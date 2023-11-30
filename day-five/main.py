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
    positional_output = {}
    value_positions  = []
    for lines in crate_lines:
        for i in range(0, len(lines)):
            if lines[i] != " " and lines[i] != "[" and lines[i] != "]":
                positional_output[i] = []
                value_positions.append((lines[i], i))
     
   
    for value in value_positions:
        for output in positional_output:
            if value[1] == output:
                positional_output[output].append(value[0])
    final_output = {}
    for output in positional_output:
        output_entry = positional_output[output]
        final_output[int(output_entry[-1])] =  output_entry[0:-1]
    
    for final in final_output:
        final_output[final].reverse()
        
    
    return dict(sorted(final_output.items()))

        

        

# return instructions in array of tuples move from to 
def transform_instructions(instructions):
    
    separate_instructions = instructions.split("\n")
    all_instructions = []
    for instruction in separate_instructions:
        split_instruction = instruction.split()
        stripped_instructions = []
        for split in split_instruction:
            if split.isnumeric():
                stripped_instructions.append(split)
        all_instructions.append(tuple(map(lambda a: int(a), stripped_instructions)))

        
    return all_instructions


def execute_instructions(instructions,  crates):
    print(crates)
    for instruction in instructions:
        crates = execute_instruction(instruction[0], instruction[1], instruction[2], crates)
    
    top_items = []
    for crate in crates:
        if len(crates[crate]) >= 1:
            top_items.append(crates[crate][-1])

    return "".join(top_items)

def execute_instruction(move,point_from, point_to, crates):
        removed_items = []

        #minus one crate in from and append it to point to
        
        for i in range(0, move):
        
            if len(crates[point_from]) >= 1:
                
                removed_crates = crates[point_from][-move:]
                for removed in removed_crates:
                    crates[point_to].append(removed)
                    crates[point_from].remove(removed)
                    

        print(crates)
        return crates
        


def read_file_contents(file_name):
    with open(file_name) as file:
        return file.read()

main()