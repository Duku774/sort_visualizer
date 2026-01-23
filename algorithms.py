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

def insertion_sort(values):
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and key < values[j]:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = key
        display(values)

def quick_sort(values, low, high):
    def partition(values, low, high):
        pivot = values[high]
        i = low - 1
        for j in range(low, high):
            if values[j] < pivot:
                i += 1
                values[i], values[j] = values[j], values[i]
                display(values)
        values[i + 1], values[high] = values[high], values[i + 1]
        display(values)
        return i + 1
    
    if low < high:
        partition_index = partition(values, low, high)
        quick_sort(values, low, partition_index - 1)
        quick_sort(values, partition_index + 1, high)

def cocktail_sort(values):
    swapped = True
    start = 0
    end = len(values)-1

    while swapped:
        swapped = False
        for i in range(start, end):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                display(values)
                swapped = True   
        if not swapped:
            break
        
        swapped = False
        end = end - 1
        for i in range(end-1, start-1, -1):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                display(values)
                swapped = True
        start = start + 1