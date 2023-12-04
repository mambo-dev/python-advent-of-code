def main():
    print("=== advent of code day seven ===")
    main_input = read_file_contents("main-input.txt")
    example_input = read_file_contents("example-input")
    largest_directories  = start_read_process(example_input) 
    print(largest_directories)

def start_read_process():
    largest_directories = []

    return largest_directories

def read_file_contents(file_name):
    with open(file_name) as file:
        return file.read()

main()