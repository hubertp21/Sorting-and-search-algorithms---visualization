import tests.main


def merge_sort(array, left, right):

    if left >= right:
        return

    mid = (left + right) // 2

    tests.main.update_plot()

    merge_sort(array, left, mid)
    merge_sort(array, mid + 1, right)

    tests.main.update_plot()

    merge(array, left, right, mid)

    tests.main.update_plot()


def merge(array, left, right, mid):

    left_cpy = array[left:mid + 1]
    right_cpy = array[mid + 1: right + 1]

    left_counter, right_counter = 0, 0
    sorted_counter = left

    while left_counter < len(left_cpy) and right_counter < len(right_cpy):

        if left_cpy[left_counter] <= right_cpy[right_counter]:
            array[sorted_counter] = left_cpy[left_counter]
            tests.main.y_vals[sorted_counter] = left_cpy[left_counter]
            left_counter += 1
        else:
            array[sorted_counter] = right_cpy[right_counter]
            tests.main.y_vals[sorted_counter] = right_cpy[right_counter]
            right_counter += 1

        sorted_counter += 1

    while left_counter < len(left_cpy):
        array[sorted_counter] = left_cpy[left_counter]
        tests.main.y_vals[sorted_counter] = left_cpy[left_counter]
        left_counter += 1
        sorted_counter += 1

    while right_counter < len(right_cpy):
        array[sorted_counter] = right_cpy[right_counter]
        tests.main.y_vals[sorted_counter] = right_cpy[right_counter]
        right_counter += 1
        sorted_counter += 1
