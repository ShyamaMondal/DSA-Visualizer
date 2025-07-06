import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import random

from sorting_algorithms import (
    bubble_sort, insertion_sort, selection_sort, merge_sort,
    quick_sort, heap_sort, counting_sort, radix_sort,
    shell_sort, bucket_sort, tim_sort
)

# Complexity dictionary
complexities = {
    "Bubble Sort":     {"Best": "O(n)",     "Avg": "O(n²)",   "Worst": "O(n²)",   "Space": "O(1)"},
    "Insertion Sort":  {"Best": "O(n)",     "Avg": "O(n²)",   "Worst": "O(n²)",   "Space": "O(1)"},
    "Selection Sort":  {"Best": "O(n²)",    "Avg": "O(n²)",   "Worst": "O(n²)",   "Space": "O(1)"},
    "Merge Sort":      {"Best": "O(n log n)", "Avg": "O(n log n)", "Worst": "O(n log n)", "Space": "O(n)"},
    "Quick Sort":      {"Best": "O(n log n)", "Avg": "O(n log n)", "Worst": "O(n²)",   "Space": "O(log n)"},
    "Heap Sort":       {"Best": "O(n log n)", "Avg": "O(n log n)", "Worst": "O(n log n)", "Space": "O(1)"},
    "Counting Sort":   {"Best": "O(n+k)",   "Avg": "O(n+k)",  "Worst": "O(n+k)",  "Space": "O(k)"},
    "Radix Sort":      {"Best": "O(nk)",    "Avg": "O(nk)",   "Worst": "O(nk)",   "Space": "O(n+k)"},
    "Shell Sort":      {"Best": "O(n log n)","Avg": "~O(n log² n)", "Worst": "O(n²)", "Space": "O(1)"},
    "Bucket Sort":     {"Best": "O(n+k)",   "Avg": "O(n+k)",  "Worst": "O(n²)",   "Space": "O(n)"},
    "Tim Sort":        {"Best": "O(n)",     "Avg": "O(n log n)", "Worst": "O(n log n)", "Space": "O(n)"}
}

# Code snippets (you can expand each if needed)
algo_code_map = {
    "Bubble Sort": """def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr""",

    "Insertion Sort": """def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            yield arr
        arr[j + 1] = key
        yield arr""",

    "Selection Sort": """def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
            yield arr
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr""",

    "Merge Sort": """def merge_sort(arr, l, r):
    if r - l > 1:
        m = (l + r) // 2
        yield from merge_sort(arr, l, m)
        yield from merge_sort(arr, m, r)
        left = arr[l:m]
        right = arr[m:r]
        i = j = 0
        for k in range(l, r):
            if i < len(left) and (j >= len(right) or left[i] <= right[j]):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            yield arr""",

    "Quick Sort": """def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        yield from quick_sort(arr, low, pivot_index - 1)
        yield from quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            yield arr
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    yield arr
    return i""",

    "Heap Sort": """def heap_sort(arr):
    import heapq
    h = []
    for value in arr:
        heapq.heappush(h, value)
    for i in range(len(arr)):
        arr[i] = heapq.heappop(h)
        yield arr""",

    "Counting Sort": """def counting_sort(arr):
    if not arr:
        return
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    i = 0
    for num in range(len(count)):
        for _ in range(count[num]):
            arr[i] = num
            i += 1
            yield arr""",

    "Radix Sort": """def radix_sort(arr):
    RADIX = 10
    maxLength = False
    tmp, placement = -1, 1
    while not maxLength:
        maxLength = True
        buckets = [list() for _ in range(RADIX)]
        for i in arr:
            tmp = i // placement
            buckets[tmp % RADIX].append(i)
            if tmp > 0:
                maxLength = False
        a = 0
        for b in range(RADIX):
            for i in buckets[b]:
                arr[a] = i
                a += 1
                yield arr
        placement *= RADIX""",

    "Shell Sort": """def shell_sort(arr):
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
        gap //= 2""",

    "Bucket Sort": """def bucket_sort(arr):
    if len(arr) == 0:
        return
    bucket_count = 10
    max_val = max(arr)
    min_val = min(arr)
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        index = (num - min_val) * (bucket_count - 1) // (max_val - min_val)
        buckets[index].append(num)
    i = 0
    for bucket in buckets:
        bucket.sort()  # You can replace this with insertion_sort(bucket) and yield
        for num in bucket:
            arr[i] = num
            i += 1
            yield arr""",

    "Tim Sort": """def tim_sort(arr):
    arr.sort()
    yield arr"""
}


class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("DSA Sorting Visualizer")
        self.width = 600
        self.height = 400

        # Layout frames
        main_frame = tk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        left_frame = tk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        right_frame = tk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # Canvas for bars
        self.canvas = tk.Canvas(left_frame, width=self.width, height=self.height, bg='white')
        self.canvas.pack()

        # Code viewer
        self.code_box = ScrolledText(right_frame, width=50, height=20, font=("Courier", 9))
        self.code_box.pack(padx=5, pady=5)

        # Algorithm dropdown
        self.algo_menu = ttk.Combobox(root, values=list(complexities.keys()), state="readonly")
        self.algo_menu.current(0)
        self.algo_menu.pack(pady=5)
        self.algo_menu.bind("<<ComboboxSelected>>", self.update_code_and_info)

        # Speed control
        ttk.Label(root, text="Animation Speed").pack()
        self.speed_scale = ttk.Scale(root, from_=1, to=10, length=200, value=5, orient=tk.HORIZONTAL)
        self.speed_scale.pack(pady=5)

        # Control buttons
        self.generate_button = ttk.Button(root, text="Generate Array", command=self.generate_array)
        self.generate_button.pack(pady=5)

        self.start_button = ttk.Button(root, text="Start Sorting", command=self.start_sorting)
        self.start_button.pack(pady=5)

        self.paused = False
        self.pause_button = ttk.Button(root, text="Pause", command=self.toggle_pause)
        self.pause_button.pack(pady=5)

        # Info and step count
        self.info_label = ttk.Label(root, text="", font=("Arial", 10))
        self.info_label.pack(pady=5)

        self.step_count = 0
        self.step_label = ttk.Label(root, text="Steps: 0", font=("Arial", 10))
        self.step_label.pack(pady=5)

        self.data = []
        self.update_code_and_info()

    def update_code_and_info(self, event=None):
        algo = self.algo_menu.get()
        self.code_box.delete("1.0", tk.END)
        self.code_box.insert(tk.END, algo_code_map.get(algo, "Code not available"))
        info = complexities.get(algo)
        if info:
            self.info_label.config(text=f"Best: {info['Best']} | Avg: {info['Avg']} | Worst: {info['Worst']} | Space: {info['Space']}")

    def generate_array(self):
        self.data = [random.randint(10, 390) for _ in range(50)]
        self.draw_array()

    def draw_array(self, color_array=None):
        if color_array is None:
            color_array = ["blue"] * len(self.data)

        self.canvas.delete("all")
        bar_width = self.width / len(self.data)
        for i, height in enumerate(self.data):
            x0 = i * bar_width
            y0 = self.height - height
            x1 = (i + 1) * bar_width
            y1 = self.height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
        self.root.update_idletasks()

    def start_sorting(self):
        algo = self.algo_menu.get()
        speed = self.speed_scale.get()
        delay = int(550 - (speed * 50))  # 1 → 500ms, 10 → 50ms

        generator = {
            "Bubble Sort": bubble_sort,
            "Insertion Sort": insertion_sort,
            "Selection Sort": selection_sort,
            "Merge Sort": lambda arr: merge_sort(arr, 0, len(arr)),
            "Quick Sort": lambda arr: quick_sort(arr, 0, len(arr) - 1),
            "Heap Sort": heap_sort,
            "Counting Sort": counting_sort,
            "Radix Sort": radix_sort,
            "Shell Sort": shell_sort,
            "Bucket Sort": bucket_sort,
            "Tim Sort": tim_sort,
        }.get(algo, lambda arr: iter([]))(self.data)

        self.step_count = 0
        self.step_label.config(text="Steps: 0")
        self.paused = False

        self.animate_sort(generator, delay)

    def toggle_pause(self):
        self.paused = not self.paused
        self.pause_button.config(text="Resume" if self.paused else "Pause")

    def animate_sort(self, generator, delay):
        if self.paused:
            self.root.after(100, lambda: self.animate_sort(generator, delay))
            return

        try:
            self.draw_array()
            next(generator)
            self.step_count += 1
            self.step_label.config(text=f"Steps: {self.step_count}")
            self.root.after(delay, lambda: self.animate_sort(generator, delay))
        except StopIteration:
            self.draw_array(["green"] * len(self.data))
