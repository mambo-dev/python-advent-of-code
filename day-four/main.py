def main():
    print("=== advent of code day 4 ===")
    main_input = read_file_contents("main-input.txt")
    example_input = read_file_contents("example-input.txt")
    print(find_pairs_fully_containing(main_input))


def find_pairs_fully_containing(file_contents):
    work_pairs = file_contents.strip().split("\n")
    count = 0
    for work_pair in work_pairs:
        lista, listb = return_lists_from_pair(work_pair)
        if (find_overlapping_list(lista, listb)):
            count += 1

    return count


def return_lists_from_pair(pairs):
    list_dict = {}
    single_pairs_list = pairs.split(",")

    for i in range(0, len(single_pairs_list)):
        list_dict[i] = transform_pair_to_list(single_pairs_list[i])

    return list_dict[0], list_dict[1]


def transform_pair_to_list(pair):
    pair_list = []

    start = int(pair.split("-")[0])
    end = int(pair.split("-")[1]) + 1

    for i in range(start, end):
        pair_list.append(i)

    return pair_list


def find_overlapping_list(arr1, arr2):
    contained_items = []
    if len(arr1) > len(arr2):
        for arr in arr1:
            if arr in arr2:
                contained_items.append(arr)
        if len(contained_items) > 0:
            return True
    else:
        for arr in arr2:
            if arr in arr1:
                contained_items.append(arr)
        if len(contained_items) > 0:
            return True

    return False


def read_file_contents(filename):
    with open(filename) as file:
        return file.read()


main()
