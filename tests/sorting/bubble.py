import tests.main


def bubble_sort(array):
    last_i = len(array) - 1  # petla wewnetrzna
    index_list = []
    tests.main.sort = "Bubble"

    for idx in range(len(array)):
        index_list.append(idx)

    tests.main.x_vals = index_list
    tests.main.y_vals = array

    for each in range(len(array)):  # petla zewn
        for i in range(last_i):
            tests.main.update_plot()
            if array[i] > array[i + 1]:  # sprawdzamy czy jest wiekszy
                array[i], array[i + 1] = array[i + 1], array[i]  # jesli tak to zamiana
                tests.main.y_vals = array

    tests.main.plt.show()
    tests.main.plt.clf()
    tests.main.plt.bar(tests.main.x_vals, tests.main.y_vals)
    tests.main.plt.xlabel("Indexes")
    tests.main.plt.ylabel("Values")
    tests.main.plt.title(tests.main.sort + " sort")
