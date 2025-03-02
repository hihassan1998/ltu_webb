from src.unorderedlist import UnorderedList
from src.sort import insertion_sort

def test_insertion_sort():
    # Create an UnorderedList instance
    unordered_list = UnorderedList()

    # Append values to the list
    unordered_list.append(5)
    unordered_list.append(2)
    unordered_list.append(9)
    unordered_list.append(1)
    unordered_list.append(7)

    print("Before sorting:")
    unordered_list.print_list()  # Prints the list before sorting

    # Sort the list using insertion_sort
    insertion_sort(unordered_list)

    print("After sorting:")
    unordered_list.print_list()  # Prints the list after sorting

# Run the test
test_insertion_sort()