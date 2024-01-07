import functools

def main():
    print("=== advent of code day seven part two ===")
    main_input = read_file_contents("main-input.txt")
    example_input = read_file_contents("example-input.txt")
    final, delete_directory  = start_read_process(main_input)
    print(delete_directory)




def start_read_process(input):
    largest_directories = []
    split_input = input.split("\n")
    directories = build_up_directory_dict(split_input)
    total_size, sizes_list = find_directory_totals(directories)

    at_most_100k = []
    for sizes in sizes_list:
        if sizes[1] <= 100000:
            at_most_100k.append(sizes[1])
    
    solution = functools.reduce(lambda a,b: a +b, at_most_100k)

    delete_directory = find_smallest_directory_to_delete(sizes_list)
    return solution, delete_directory

def find_smallest_directory_to_delete(directories_list):
    space_needed_for_update = 30000000
    full_space = 70000000
    total_space_used = directories_list[0][1]
    remaining_space = full_space - total_space_used
    space_to_be_cleared = space_needed_for_update - remaining_space
    size_to_be_deleted = 0
    all_eligible_sizes = []
    for directory in directories_list:
        size = directory[1]
        if size >= space_to_be_cleared:
            all_eligible_sizes.append(size)
            
    all_eligible_sizes.sort()
   
    return all_eligible_sizes[0]

    

def find_directory_totals(directories):
    
    total_size = 0
    sizes_list = []
    for item, value in directories.items():
        if isinstance(value, dict):
            sub_dir_size, subdirectory_sizes = find_directory_totals(value)
            total_size += sub_dir_size
    
            sizes_list.append((item, sub_dir_size))
            sizes_list.extend(subdirectory_sizes)
        else:
            total_size += value

    
    return total_size, sizes_list

    


def build_up_directory_dict(split_input):
    directories = {}
    current_directory = directories
    stack = []
    for i in range(0, len(split_input)):
        line = split_input[i]
        instruction = ""
        if line.startswith("$"):
             instruction = line.split()[1]

    
        if instruction == "cd":
            directory = line.split()[2]
            if directory == "..":
                stack.pop()
                current_directory = stack[-1] if len(stack) > 0 else directories["/"]
            else:
                current_directory[f"dir-{directory}"] = {}
                current_directory = current_directory[f"dir-{directory}"]
                stack.append(current_directory)
        elif instruction == "ls":
            i += 1
            while i < len(split_input):
                next_line = split_input[i]
                if next_line.startswith("$"):
                    # a command so we break from current loop
                    break
                else:
                    file_or_directory = (split_input[i].split()[0],split_input[i].split()[1])
                    if file_or_directory[0] == "dir":
                        current_directory[f"dir-{file_or_directory[1]}"] = {}
                    else:
                        current_directory[f"file-{file_or_directory[1]}"] = int(file_or_directory[0])

                
                i += 1 

    return directories

            


def read_file_contents(file_name):
    try:
        with open(file_name) as file:
            return file.read()
    except FileNotFoundError:
        raise Exception("The file you are trying to open was not found")

main()