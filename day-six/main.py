def main():
    example_input = read_file_contents("example-input.txt")
    main_input = read_file_contents("main-input.txt")
    


def read_file_contents(file_name):
    with open(file_name) as file:
        return file.read()

main()