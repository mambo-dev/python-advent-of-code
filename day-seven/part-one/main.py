def main():
    print("=== advent of code day seven ===")
    main_input = read_file_contents("main-input.txt")
    example_input = read_file_contents("example-input.txt")
    largest_directories  = start_read_process(example_input) 


def start_read_process(input):
    largest_directories = []
    split_input = input.split("\n")
    directories = {}
    current_directory = ""
    for i in range(0, len(split_input)):
        line = split_input[i]
        if line.startswith("$"):
            instruction = line.split()[1]
            if instruction == "cd":
                directory = line.split()[2]
                current_directory = directory

          

                    
               
    print("this is directories tree", directories)
        

    return largest_directories

def read_file_contents(file_name):
    try:
        with open(file_name) as file:
            return file.read()
    except FileNotFoundError:
        raise Exception("The file you are trying to open was not found")

main()