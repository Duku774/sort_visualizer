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

def heap_sort(values):
    def heapify(array, array_len, root):
        largest = root
        left_index = 2 * root + 1
        right_index = 2 * root + 2

        if left_index < array_len and array[left_index] > array[largest]:
            largest = left_index
        if right_index < array_len and array[right_index] > array[largest]:
            largest = right_index

        if largest != root:
            array[root], array[largest] = array[largest], array[root]
            display(array)
            heapify(array, array_len, largest)

    for i in range(len(values) // 2 - 1, -1, -1):
        heapify(values, len(values), i)
    
    for i in range(len(values) - 1, 0, -1):
        values[0], values[i] = values[i], values[0]
        display(values)
        heapify(values, i, 0)

def radix_sort(values):
    def digit_sort(array, exp):
        output = [0] * len(array)
        count = [0] * 10

        for i in range (0, len(array)):
            index = array[i] // exp
            count[int(index % 10)] += 1
        for i in range(1, 10):
            count[i] += count [i - 1]

        i = len(array) - 1
        while i >= 0:
            index = array[i] // exp
            output[count[int(index % 10)] - 1] = array[i]
            count[int(index % 10)] -= 1
            i -= 1

        i = 0
        for i in range (0, len(array)):
            array[i] = output[i]
            display(array)

    exponential = 1
    while max(values) // exponential >= 1:
        digit_sort(values, exponential)
        exponential *= 10

def comb_sort(values):
    def get_next_gap(gap):
        gap = (gap * 10) // 13
        if gap < 1:
            return 1
        return gap
    
    gap = len(values)
    swapped = True
    while gap != 1 or swapped:
        gap = get_next_gap(gap)
        swapped = False
        for i in range(0, len(values) - gap):
            if values[i] > values[i + gap]:
                values[i], values[i + gap] = values[i + gap], values[i]
                display(values)
                swapped = True

def shell_sort(values):
    gap = len(values) // 2
    while gap > 0:
        for i in range(gap, len(values)):
            temp = values[i]
            j = i
            while j >= gap and values[j - gap] > temp:
                values[j] = values[j - gap]
                j -= gap
                display(values)
            values[j] = temp
        gap //= 2