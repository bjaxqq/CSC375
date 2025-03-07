def find_closest_k(A, x, k):
    differences = []
    
    for num in A:
        diff = abs(num - x)
        differences.append(diff, num)

    def min_heap(arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
    
    def heapify(arr, n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left][0] < arr[smallest][0]:
            smallest = left

        if right < n and arr[right][0] < arr[smallest][0]:
            smallest = right

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            heapify(arr, n, smallest)

    def get_min(arr):
        n = len(arr)
        if n == 0:
            return None
        
        min_element = arr[0]
        arr[0] = arr[n - 1]
        arr.pop()
        heapify(arr, n - 1, 0)
        
        return min_element

    build_min_heap(differences)
    result = []

    for _ in range(k):
        diff, num = extract_min(differences)
        result.append(num)
        return result

"""
Analysis:

To get the O(n + k log n), I compare the absolute difference between elements in A and x and store pairs in a list.
Then I build the min heap list of differences to get the smallest difference at the heap's root.
Then I extract k closest k numbers from the heap and add to the result.
With computing the differences being Θ(n), the heap building being Θ(n), and the extract being Θ(k log n), we get:

Θ(n + k log n)
"""