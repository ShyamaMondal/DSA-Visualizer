## Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr

## Merge Sort
def merge_sort(arr, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        yield from merge_sort(arr, start, mid)
        yield from merge_sort(arr, mid, end)
        left = arr[start:mid]
        right = arr[mid:end]
        k = start
        i = j = 0
        while start + i < mid and mid + j < end:
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            yield arr
        while start + i < mid:
            arr[k] = left[i]
            i += 1
            k += 1
            yield arr
        while mid + j < end:
            arr[k] = right[j]
            j += 1
            k += 1
            yield arr

## Quick Sort
def quick_sort(arr, low, high):
    if low < high:
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                yield arr
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        yield arr
        yield from quick_sort(arr, low, i - 1)
        yield from quick_sort(arr, i + 1, high)

## Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            yield arr
        arr[j + 1] = key
        yield arr

##Selection Sort        
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
            yield arr
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr

##Heap Sort
def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        yield arr
        yield from heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        yield arr
        yield from heapify(arr, i, 0)

## Counting Sort (only for positive integers)
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1
        yield arr

    i = 0
    for num, freq in enumerate(count):
        for _ in range(freq):
            arr[i] = num
            i += 1
            yield arr

## Radix Sort
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in arr:
        index = (i // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]
        yield arr

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        yield from counting_sort_for_radix(arr, exp)
        exp *= 10

## Shell Sort
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                yield arr
            arr[j] = temp
            yield arr
        gap //= 2

## Bucket Sort (Good for uniform distributions)
def bucket_sort(arr):
    if len(arr) == 0:
        return

    bucket_count = 10
    max_val = max(arr)
    min_val = min(arr)
    bucket_range = (max_val - min_val) / bucket_count + 1

    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int((num - min_val) / bucket_range)
        buckets[index].append(num)
        yield arr

    i = 0
    for bucket in buckets:
        bucket.sort()
        for num in bucket:
            arr[i] = num
            i += 1
            yield arr

##Tim Sort (used in Python’s built-in sort())
def tim_sort(arr):
    arr.sort()  # Python’s built-in TimSort
    yield arr
