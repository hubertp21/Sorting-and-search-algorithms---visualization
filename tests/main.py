import matplotlib.pyplot as plt
import gui

plt.style.use("fivethirtyeight")

x_vals = []
y_vals = []
sort = ""
search = ""


def update_plot():
    plt.clf()
    plt.bar(x_vals, y_vals)
    plt.xlabel("Indexes")
    plt.ylabel("Values")
    plt.title(sort + " sort")
    plt.pause(0.01)


def update_search(i, searched):

    if searched:
        plt.clf()
        barlist = plt.bar(x_vals, y_vals)
        text = "i = "+str(i)+". Value has been found!"
        plt.text(12.5, max(y_vals) - 1, text, horizontalalignment='center',
                 verticalalignment='center')
        barlist[i].set_color("y")
        plt.xlabel("Indexes")
        plt.ylabel("Values")
        plt.title(search + " search")
        plt.pause(0.1)

    else:
        plt.clf()
        barlist = plt.bar(x_vals, y_vals)
        text = "i = " + str(i)+". Value not found :("
        plt.text(12.5, max(y_vals) - 1, text, horizontalalignment='center',
                 verticalalignment='center')
        barlist[i].set_color("r")
        plt.xlabel("Indexes")
        plt.ylabel("Values")
        plt.title(search + " search")
        plt.pause(0.1)


def start():
    gui.root.mainloop()


if __name__ == "__main__":
    start()
    exit(1)
