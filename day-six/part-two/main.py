def main():
    example_input = read_file_contents("../example-input.txt")
    main_input = read_file_contents("../main-input.txt")

    position_found = start_of_message(main_input)
    print("found at position", position_found)


def start_of_message(input):
    store_inputs = {}
    found_at  = ""
    duplicate_found_at = 0
    first_marker = 0
    store_four_from_current_index = []
    for i in range(0,len(input)):
        next_idx = i + 1
        for j in range(i , i + 14):
            
            store_four_from_current_index.append(input[j])
            if len(store_four_from_current_index) == 14:
                if is_unique(store_four_from_current_index):
                    first_marker = store_four_from_current_index[-1]
                    store_four_from_current_index.clear()
                   
                    return i + 14
                else:
            
                    next_idx, i =  i, next_idx
                    store_four_from_current_index.clear()
           

    
          

    return first_message_marker

def is_unique(lst):
    return len(lst) == len(set(lst))


def read_file_contents(file_name):
    with open(file_name) as file:
        return file.read()

main()