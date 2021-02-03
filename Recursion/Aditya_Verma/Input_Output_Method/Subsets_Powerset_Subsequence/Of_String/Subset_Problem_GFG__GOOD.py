# https://practice.geeksforgeeks.org/problems/subsets/0

def get_unique_subset(input, output, all_subsets, index):
    if index >= len(input):
        # sort this output, which is a tuple
        current_subset = list(output)
        current_subset.sort()

        all_subsets.add(tuple(current_subset))  # so all_subsets will be a set of tuples
        return

    output_when_did_not_choose = output
    output_when_chosen = output + (input[index],)  # creating another tuple to concatenate with

    get_unique_subset(input, output_when_chosen, all_subsets, index + 1)
    get_unique_subset(input, output_when_did_not_choose, all_subsets, index + 1)


def print_in_required_for(all_subset_list):
    final_output = []
    for subset in all_subset_list:
        final_output.append('(')
        for index, element in enumerate(subset):

            final_output.append(str(element))
            if index != len(subset) - 1:
                final_output.append(' ')
        final_output.append(')')
        # final_output.append(' ')

    final_string = ''.join(final_output)

    print(final_string.strip())


def print_unique_lexicographically_sorted_subset(input):
    # Not using output as string, as then we would require to convert them back to integer
    output = tuple()  # The reason to use tuple is they are immutable,
    # and if i used List i would have to use indexing inside that as well

    set_of_all_subsets = set()
    starting_index = 0
    get_unique_subset(input, output, set_of_all_subsets, starting_index)
    # print(set_of_all_subsets)

    all_subset_list = list(set_of_all_subsets)
    all_subset_list.sort()
    # print(all_subset_list)

    print_in_required_for(all_subset_list)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        nums = list(map(int, input().strip().split(" ")))

        print_unique_lexicographically_sorted_subset(nums)
