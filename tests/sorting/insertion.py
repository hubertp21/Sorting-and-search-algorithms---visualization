import tests.main


def insertion_sort(array):
    length = len(array)

    index_list = []
    tests.main.sort = "Insertion"

    for idx in range(len(array)):
        index_list.append(idx)

    tests.main.x_vals = index_list
    tests.main.y_vals = array

    for i in range(1, length):  # petla zewn, liczymy od 1 bo poprzednik
        j = i - 1  # poprzednik

        successor = array[i]  # zapisujemy wartosc zmiennej

        while successor < array[j] and j >= 0:  # jesli jest mniejsza to:
            tests.main.update_plot()
            array[j + 1] = array[j]  # dajemy wartosc wieksza na indeks rowny i
            j = j - 1  # jesli dalej jest mniejsza
            tests.main.y_vals = array
        array[j + 1] = successor  # po unkonczeniu petli zapisujemy wartosc

        tests.main.plt.show()
        tests.main.plt.clf()
        tests.main.plt.bar(tests.main.x_vals, tests.main.y_vals)
        tests.main.plt.xlabel("Indexes")
        tests.main.plt.ylabel("Values")
        tests.main.plt.title(tests.main.sort + " sort")
