from tkinter import *
from visualization import visualize_bubble, visualize_insertion, visualize_merge, visualize_shell, visualize_binary, visualize_basic, visualize_interpolation
import random

starting_number = 1
starting_number_inserted = False
last_number = 80
last_number_inserted = False
number_of_elements = 25
number_of_elements_inserted = False
searched = random.randint(1, 80)
sort_type = ""
search_type = ""


def sorting():
    sorting_gui = Tk()
    sorting_gui.title("Sorting algorhitms")
    bubble_sort = Button(sorting_gui, text="Bubble sort", padx=85, pady=40, command=get_bubble)
    bubble_sort.pack()

    insertion_sort = Button(sorting_gui, text="Insertion sort", padx=85, pady=40, command=get_insertion)
    insertion_sort.pack()

    merge_sort = Button(sorting_gui, text="Merge sort", padx=85, pady=40, command=get_merge)
    merge_sort.pack()

    shell_sort = Button(sorting_gui, text="Shell sort", padx=85, pady=40, command=get_shell)
    shell_sort.pack()


def search():
    searching_gui = Tk()
    searching_gui.title("Searching algorhitms")
    basic_search = Button(searching_gui, text="Basic search", padx=85, pady=40, command=visualize_basic)
    binary_search = Button(searching_gui, text="Binary search", padx=85, pady=40, command=visualize_binary)
    interpolation_search = Button(searching_gui, text="Interpolation search", padx=85, pady=40,
                                  command=visualize_interpolation)

    basic_search.pack()
    binary_search.pack()
    interpolation_search.pack()


def close():
    root.destroy()
    exit(1)


def get_bubble():
    global sort_type
    sort_type = "bubble"
    start_sorting()


def get_insertion():
    global sort_type
    sort_type = "insertion"
    start_sorting()


def get_merge():
    global sort_type
    sort_type = "merge"
    start_sorting()


def get_shell():
    global sort_type
    sort_type = "shell"
    start_sorting()


def start_sorting():
    starting_gui = Tk()

    add_starting_number_label = Label(starting_gui, text='Enter the smallest number in array', font=('calibre', 10, 'bold'))
    add_starting_number_label.grid(row=0, column=0)
    default_starting_number_label = Label(starting_gui, text='Default value: 1', font=('calibre', 10, 'bold'))
    default_starting_number_label.grid(row=0, column=2)
    e_s = Entry(starting_gui, width=35, borderwidth=5)
    e_s.grid(row=0, column=1)

    add_last_number_label = Label(starting_gui, text='Enter the biggest number in array', font=('calibre', 10, 'bold'))
    add_last_number_label.grid(row=1, column=0)
    default_last_number_label = Label(starting_gui, text='Default value: 80', font=('calibre', 10, 'bold'))
    default_last_number_label.grid(row=1, column=2)
    e_l = Entry(starting_gui, width=35, borderwidth=5)
    e_l.grid(row=1, column=1)

    add_number_of_elements_label = Label(starting_gui, text='Enter number of elements in array', font=('calibre', 10, 'bold'))
    add_number_of_elements_label.grid(row=2, column=0)
    default_number_of_elements_label = Label(starting_gui, text='Default value: 25', font=('calibre', 10, 'bold'))
    default_number_of_elements_label.grid(row=2, column=2)
    e_n = Entry(starting_gui, width=35, borderwidth=5)
    e_n.grid(row=2, column=1)

    def add_starting_number():
        global starting_number, starting_number_inserted
        starting_number = int(e_s.get())
        starting_number_inserted = True
        e_s.delete(0, END)

    def add_last_number():
        global last_number, last_number_inserted
        last_number = int(e_l.get())
        last_number_inserted = True
        e_l.delete(0, END)

    def add_number_of_elements():
        global number_of_elements, number_of_elements_inserted
        number_of_elements = int(e_n.get())
        number_of_elements_inserted = True
        e_n.delete(0, END)

    global sort_type
    if sort_type == "bubble":
        start_button = Button(starting_gui, text="Start", padx=85, pady=40, command=visualize_bubble)
        start_button.grid(row=3, column=1)
    elif sort_type == "insertion":
        start_button = Button(starting_gui, text="Start", padx=85, pady=40, command=visualize_insertion)
        start_button.grid(row=3, column=1)
    elif sort_type == "merge":
        start_button = Button(starting_gui, text="Start", padx=85, pady=40, command=visualize_merge)
        start_button.grid(row=3, column=1)
    elif sort_type == "shell":
        start_button = Button(starting_gui, text="Start", padx=85, pady=40, command=visualize_shell)
        start_button.grid(row=3, column=1)

    get_starting_number = Button(starting_gui, text="Get the smallest number", padx=85, pady=40,
                                 command=add_starting_number)
    get_starting_number.grid(row=4, column=0)

    get_last_number = Button(starting_gui, text="Get the biggest number", padx=85, pady=40, command=add_last_number)
    get_last_number.grid(row=4, column=1)

    get_number_of_elements = Button(starting_gui, text="Get the number of elements", padx=85, pady=40, command=add_number_of_elements)
    get_number_of_elements.grid(row=4, column=2)


root = Tk()
root.title("Algorithms - visualised")

sorting_algorhitms = Button(root, text="Sorting algorhitms", padx=84, pady=40, command=sorting)
search_algorhitms = Button(root, text="Search algorithms", padx=86, pady=40, command=search)
close_button = Button(root, text="Exit app", padx=112, pady=40, command=close)

sorting_algorhitms.pack()
search_algorhitms.pack()
close_button.pack()
