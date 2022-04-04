import tests.main
from time import sleep


def interpolation_search(array, val):
    searched = False

    tests.main.search = "Interpolation"
    index_list = []

    for idx in range(len(array)):
        index_list.append(idx)

    tests.main.x_vals = index_list
    tests.main.y_vals = array

    (left, right) = (0, len(array) - 1)

    while array[right] != array[left] and array[left] <= val <= array[right]:

        mid = left + (val - array[left]) * (right - left) // (array[right] - array[left])
        tests.main.update_search(mid, searched)
        sleep(0.1)
        if val == array[mid]:
            searched = True
            tests.main.update_search(mid, searched)
            break

        elif val < array[mid]:
            right = mid - 1

        else:
            left = mid + 1

    if val == array[left]:
        searched = True
        tests.main.update_search(left, searched)
