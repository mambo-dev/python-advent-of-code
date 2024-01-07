def main():
    print("=== advent of code day seven ===")
    main_input = read_file_contents("main-input.txt")
    example_input = read_file_contents("example-input.txt")
    largest_directories  = start_read_process(example_input) 


def start_read_process(input):
    largest_directories = []
    split_input = input.split("\n")
    directories = build_up_directory_dict(split_input)
    


def build_up_directory_dict(split_input):
    directories = {}
    current_directory = directories
    stack = []
    for i in range(0, len(split_input)):
        line = split_input[i]
        instruction = ""
        if line.startswith("$"):
             instruction = line.split()[1]

    
        if instruction == "cd":
            directory = line.split()[2]
            if directory == "..":
                stack.pop()
                current_directory = stack[-1] if len(stack) > 0 else directories["/"]
            else:
                current_directory[directory] = {}
                current_directory = current_directory[directory]
                stack.append(current_directory)
        elif instruction == "ls":
            i += 1
            while i < len(split_input):
                next_line = split_input[i]
                if next_line.startswith("$"):
                    # a command so we break from current loop
                    break
                else:
                    file_or_directory = (split_input[i].split()[0],split_input[i].split()[1])
                    if file_or_directory[0] == "dir":
                        current_directory[file_or_directory[1]] = {}
                    else:
                        current_directory[file_or_directory[1]] = int(file_or_directory[0])
                
                i += 1 

    return directories

            


def read_file_contents(file_name):
    try:
        with open(file_name) as file:
            return file.read()
    except FileNotFoundError:
        raise Exception("The file you are trying to open was not found")

main()