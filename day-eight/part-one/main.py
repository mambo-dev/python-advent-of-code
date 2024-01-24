
def main():
    print("=== advent of code day 8 ===")
    main_contents = read_file_contents("main-input.txt")
    example_contents = read_file_contents("example-input.txt")
    total_visible = start_execution_process(example_contents)


def start_execution_process(file_contents):
    raw_data = file_contents.split("\n")
    tree_grid = create_tree_grid(raw_data)
    print(tree_grid)

    return 0

def create_tree_grid(raw_data):
    grid = []
    for row in raw_data:
        append_row = []
        for each_row in row:
            append_row.append(int(each_row))
        grid.append(append_row)  


    return grid




def read_file_contents(file_name):
    try:
        with open(file_name) as file:
            return file.read()

    except FileNotFoundError:
        raise Exception("The file you are trying to open was not found")


main()