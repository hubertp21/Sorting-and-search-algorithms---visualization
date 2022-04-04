import tests.main


def binary_search(array, val):
    searched = False

    tests.main = tests.main
    tests.main.search = "Binary"
    index_list = []

    for idx in range(len(array)):
        index_list.append(idx)

    tests.main.x_vals = index_list
    tests.main.y_vals = array

    low = 0
    high = len(array) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2
        tests.main.update_search(mid, searched)

        if array[mid] < val:
            low = mid + 1

        elif array[mid] > val:
            high = mid - 1

        else:
            searched = True
            tests.main.update_search(mid, searched)
            break
