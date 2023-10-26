def main():
    print("=== advent of code day 4 ===")
    main_input = read_file_contents("main-input.txt")
    example_input = read_file_contents("example-input.example-input.txt")


def read_file_contents(filename):
    with open(filename) as file:
        return file.read()


main()
