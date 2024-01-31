
def main():
    print("=== advent of code day 8 ===")
    main_contents = read_file_contents("main-input.txt")
    example_contents = read_file_contents("example-input.txt")
    scenic_score = start_execution_process(main_contents)
    print("highest possible score is ",scenic_score)


def start_execution_process(file_contents):
    raw_data = file_contents.split("\n")
    tree_grid = create_tree_grid(raw_data)
    scenic_score = get_scenic_score(tree_grid)


    return scenic_score

def get_scenic_score(tree_grid):
    tree_tuple = []

    for i in range(1, len(tree_grid) -1):
        # tuple with numbers and their index
        for j in range(1, len(tree_grid[i]) -1 ):
            tree_height = tree_grid[i][j]
            tree_tuple.append((i, j, tree_height))

    scenic_scores = []
    for item in tree_tuple:
        row = tree_grid[item[0]]
        current_tree = tree_grid[item[0]][item[1]]
        left_visible, left_seen = check_left(current_tree, row, item[1])
        right_visible, right_seen = check_right(current_tree, row, item[1])
        top_visible,top_seen = check_top(tree_grid,current_tree,item[0],item[1])
        bottom_visible,bottom_seen = check_bottom(tree_grid,current_tree,item[0],item[1])
        current_tree_score = bottom_seen * left_seen * right_seen * top_seen
        scenic_scores.append(current_tree_score)
        

    highest_possible_score = sorted(scenic_scores)[-1]
    return highest_possible_score

def check_left(current_tree, row, current_tree_idx):
    visible = True
    previous_idx = current_tree_idx - 1
    trees_seen = 0
   
    while previous_idx >= 0 and visible is True:
        if current_tree > row[previous_idx]:
            visible = True
        else:
            visible = False
        
        trees_seen += 1
        previous_idx -= 1
    
    return visible,trees_seen

def check_right(current_tree, row, current_tree_idx):
    visible = True
    next_idx = current_tree_idx + 1
    trees_seen = 0
    while next_idx <= len(row) - 1 and visible is True :
        if current_tree > row[next_idx]:
            visible = True
        else:
            visible = False
        trees_seen += 1
        next_idx += 1

    return visible,trees_seen

def check_bottom(grid, current_tree, row_idx, current_tree_idx):
    visible = True
    check_idx = current_tree_idx
    next_row = row_idx + 1
    trees_seen = 0
    while next_row <= len(grid) - 1 and visible is True:
        if grid[next_row][check_idx] < current_tree:
            visible = True
        else:
            visible = False
        trees_seen += 1
        next_row += 1


    return visible,trees_seen

def check_top(grid, current_tree, row_idx, current_tree_idx):
    visible = True
    check_idx = current_tree_idx
    previous_row = row_idx - 1
    trees_seen = 0
    while previous_row >= 0 and visible is True:
        if grid[previous_row][check_idx] < current_tree:
            visible = True
        else:
            visible = False
        trees_seen += 1
        previous_row -= 1


    return visible,trees_seen




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