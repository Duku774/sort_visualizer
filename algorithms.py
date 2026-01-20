from visualizer import *

def bubble_sort(values):
    for i in range(len(values) - 1):
        for j in range(len(values) - i - 1):
            if values[j] > values[j + 1]:
                t = values[j]
                values[j] = values[j + 1]
                values[j + 1] = t
            display(values)

def selection_sort(values):
    for i in range(len(values) - 1):
        min_idx = i
        for j in range(i + 1, len(values)):
            if values[j] < values[min_idx]:
                min_idx = j
        values[i], values[min_idx] = values[min_idx], values[i]
        display(values)