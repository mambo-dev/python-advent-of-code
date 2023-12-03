def main():
    example_input = read_file_contents("../example-input.txt")
    main_input = read_file_contents("../main-input.txt")

    position_found = start_sub_routine(main_input)
    print("found at position", position_found)

def start_sub_routine(input):
    store_inputs = {}
    found_at  = ""
    duplicate_found_at = 0
    first_marker = 0
    store_four_from_current_index = []
    for i in range(0,len(input)):
        next_idx = i + 1
        for j in range(i , i + 4):
            
            store_four_from_current_index.append(input[j])
            if len(store_four_from_current_index) == 4:
                if is_unique(store_four_from_current_index):
                    first_marker = store_four_from_current_index[-1]
                    store_four_from_current_index.clear()
                   
                    return i + 4
                else:
            
                    next_idx, i =  i, next_idx
                    store_four_from_current_index.clear()
           

    
          

    return first_marker

def is_unique(lst):
    return len(lst) == len(set(lst))


def read_file_contents(file_name):
    with open(file_name) as file:
        return file.read()

main()