
def main():
    print("=== advent of code day 8 ===")
    main_contents = read_file_contents("main-input.txt")
    example_contents = read_file_contents("example-input.txt")
    total_visible = start_execution_process(example_contents)
    print("We can see",total_visible)


def start_execution_process(file_contents):
    raw_data = file_contents.split("\n")
    tree_grid = create_tree_grid(raw_data)
    edge_count = count_visible_edges(tree_grid)
    interior_count = count_interior_visible(tree_grid)


    return edge_count + interior_count

def count_interior_visible(tree_grid):
    tree_tuple = []
    for i in range(1, len(tree_grid) -1):
        # tuple with numbers and their index
        for j in range(1, len(tree_grid[i]) -1 ):
            tree_height = tree_grid[i][j]
            tree_tuple.append((i, j, tree_height))

    print(tree_tuple)
    for item in tree_tuple:
        rows = tree_grid[item[0]]
        current_tree_height = rows[item[1]]


    return 0


def count_visible_edges(tree_grid):
    top_row = len(tree_grid[0])
    
    side_row = 0
    for i in range(1, len(tree_grid) -1):
        
        side_row += 1

    
    return (top_row * 2) + (side_row * 2)


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