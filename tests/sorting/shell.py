import tests.main


def shell_sort(array):
    index_list = []

    tests.main.sort = "Shell"

    for idx in range(len(array)):
        index_list.append(idx)

    tests.main.x_vals = index_list
    tests.main.y_vals = array

    interval = 1

    while interval < len(array)//3:
        interval = interval * 3 + 1
    while interval > 0:

        for i in range(interval, len(array)):

            tests.main.update_plot()

            j = i - interval

            successor = array[i]

            while j >= 0 and successor < array[j]:
                array[j+interval] = array[j]
                tests.main.y_vals[j + interval] = array[j]
                j = j - interval
            tests.main.y_vals[j + interval] = successor
        interval = int((interval - 1) // 3)

        tests.main.plt.show()
        tests.main.plt.clf()
        tests.main.plt.bar(tests.main.x_vals, tests.main.y_vals)
        tests.main.plt.xlabel("Indexes")
        tests.main.plt.ylabel("Values")
        tests.main.plt.title(tests.main.sort + " sort")
