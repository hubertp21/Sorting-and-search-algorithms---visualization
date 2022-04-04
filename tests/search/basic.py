import tests.main


def basic_search(array, val):

    searched = False

    tests.main.search = "Basic"
    index_list = []

    for idx in range(len(array)):
        index_list.append(idx)

    tests.main.x_vals = index_list
    tests.main.y_vals = array

    for i in range(0, len(array)):
        if array[i] == val:
            searched = True
            tests.main.update_search(i, searched)
            break
        tests.main.update_search(i, searched)


