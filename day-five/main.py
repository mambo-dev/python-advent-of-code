def main():
    print("=== advent of code day five ===")
    main_input = read_file_contents("main-input.txt")
    example_input = read_file_contents("example-input.txt")
    split_crates_and_instructions(example_input)

#split the instructions and crates into two pieces i can use
def split_crates_and_instructions(file_contents):
 
    split_contents = file_contents.split("\n\n")
    crates_ = split_contents[0]
    instructions = split_contents[1]
    crates_dict = {}

    return transform_crates(crates), transform_instructions(instructions)

def transform_crates(crates):
    print("crates", crates)

def transform_instructions(instructions):
    print("instructions", instructions)


def execute_instructions(move, point_from, point_to, crates):

    return True

def read_file_contents(file_name):
    with open(file_name) as file:
        return file.read()

main()