
def main():
    print("=== advent of code day 8 ===")
    main_contents = read_file_contents("main-input.txt")
    example_contents = read_file_contents("example-input.txt")
    total_visible = start_execution_process(main_contents)
    print("We can see",total_visible)


def start_execution_process(file_contents):
    raw_data = file_contents.split("\n")
    tree_grid = create_tree_grid(raw_data)
    edge_count = count_visible_edges(tree_grid)
    interior_count = count_interior_visible(tree_grid)


    return edge_count + interior_count

def count_interior_visible(tree_grid):
    tree_tuple = []
    visible_trees =  []
    for i in range(1, len(tree_grid) -1):
        # tuple with numbers and their index
        for j in range(1, len(tree_grid[i]) -1 ):
            tree_height = tree_grid[i][j]
            tree_tuple.append((i, j, tree_height))


    for item in tree_tuple:
        row = tree_grid[item[0]]
        current_tree = tree_grid[item[0]][item[1]]
        left_visible = check_left(current_tree, row, item[1])
        right_visible = check_right(current_tree, row, item[1])
        top_visible = check_top(tree_grid,current_tree,item[0],item[1])
        bottom_visible = check_bottom(tree_grid,current_tree,item[0],item[1])
        

        if right_visible or left_visible or top_visible or bottom_visible:
            visible_trees.append(current_tree)
        


    return len(visible_trees)

def check_left(current_tree, row, current_tree_idx):
    visible = True
    previous_idx = current_tree_idx - 1
    while previous_idx >= 0 and visible is True:
        if current_tree > row[previous_idx]:
            visible = True
        else:
            visible = False

        previous_idx -= 1
    
    return visible

def check_right(current_tree, row, current_tree_idx):
    visible = True
    next_idx = current_tree_idx + 1
    while next_idx <= len(row) - 1 and visible is True :
        if current_tree > row[next_idx]:
            visible = True
        else:
            visible = False

        next_idx += 1
    
    return visible

def check_bottom(grid, current_tree, row_idx, current_tree_idx):
    visible = True
    check_idx = current_tree_idx
    next_row = row_idx + 1
    while next_row <= len(grid) - 1 and visible is True:
        if grid[next_row][check_idx] < current_tree:
            visible = True
        else:
            visible = False

        next_row += 1


    return visible

def check_top(grid, current_tree, row_idx, current_tree_idx):
    visible = True
    check_idx = current_tree_idx
    previous_row = row_idx - 1
    while previous_row >= 0 and visible is True:
        if grid[previous_row][check_idx] < current_tree:
            visible = True
        else:
            visible = False

        previous_row -= 1


    return visible


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