from sorting import bubble, insertion, merge, shell
from search import basic, binary, interpolation
import random
import gui
from tests import main


def visualize_bubble():

    arr = []
    for i in range(0, gui.number_of_elements):
        arr.append(random.randint(gui.starting_number, gui.last_number))

    bubble.bubble_sort(arr)
    if gui.starting_number_inserted:
        gui.starting_number = 1
        gui.starting_number_inserted = False
    if gui.last_number_inserted:
        gui.last_number = 80
        gui.last_number_inserted = False
    if gui.number_of_elements_inserted:
        gui.number_of_elements = 25
        gui.number_of_elements_inserted = False


def visualize_insertion():

    arr = []
    for i in range(0, gui.number_of_elements):
        arr.append(random.randint(gui.starting_number, gui.last_number))

    insertion.insertion_sort(arr)
    if gui.starting_number_inserted:
        gui.starting_number = 1
        gui.starting_number_inserted = False
    if gui.last_number_inserted:
        gui.last_number = 80
        gui.last_number_inserted = False
    if gui.number_of_elements_inserted:
        gui.number_of_elements = 25
        gui.number_of_elements_inserted = False


def visualize_merge():

    arr = []
    for i in range(0, gui.number_of_elements):
        arr.append(random.randint(gui.starting_number, gui.last_number))

    main.sort = "Merge"

    index_list = []

    for idx in range(len(arr)):
        index_list.append(idx)
    main.x_vals = index_list
    main.y_vals = arr

    merge.merge_sort(arr, 0, len(arr))
    if gui.starting_number_inserted:
        gui.starting_number = 1
        gui.starting_number_inserted = False
    if gui.last_number_inserted:
        gui.last_number = 80
        gui.last_number_inserted = False
    if gui.number_of_elements_inserted:
        gui.number_of_elements = 25
        gui.number_of_elements_inserted = False


def visualize_shell():
    arr = []
    for i in range(0, gui.number_of_elements):
        arr.append(random.randint(gui.starting_number, gui.last_number))

    shell.shell_sort(arr)
    if gui.starting_number_inserted:
        gui.starting_number = 1
        gui.starting_number_inserted = False
    if gui.last_number_inserted:
        gui.last_number = 80
        gui.last_number_inserted = False
    if gui.number_of_elements_inserted:
        gui.number_of_elements = 25
        gui.number_of_elements_inserted = False


def visualize_basic():
    arr = []
    for i in range(0, 25):
        arr.append(random.randint(1, 80))

    basic.basic_search(arr, random.randint(1, 80))


def visualize_binary():
    arr = []
    for i in range(0, 25):
        arr.append(random.randint(1, 80))

    arr.sort()
    binary.binary_search(arr, random.randint(1, 80))


def visualize_interpolation():
    arr = []
    for i in range(0, 25):
        arr.append(random.randint(1, 80))

    arr.sort()
    interpolation.interpolation_search(arr, random.randint(1, 80))
