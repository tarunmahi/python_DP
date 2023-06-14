"""
    There are two main types of heaps: min-heap and max-heap.

Min-Heap: In a min-heap, the value of each node is greater than or equal to the values of its children. The root node contains the minimum value in the heap.

Max-Heap: In a max-heap, the value of each node is less than or equal to the values of its children. The root node contains the maximum value in the heap.

Heaps are commonly implemented using arrays, where the parent-child relationships are maintained based on the indices of the array elements.

Key operations on a heap include:

Insertion: Adding a new element to the heap. The element is placed at the next available position in the array, and then it is "bubbled up" or "sifted up" to its correct position to maintain the heap property.

Extraction: Removing the root element (the highest or lowest priority element) from the heap. The last element in the array is moved to the root position, and then it is "bubbled down" or "sifted down" to its correct position to maintain the heap property.

Peek: Accessing the value of the root element without removing it from the heap.

The time complexity of the basic heap operations is as follows:

Insertion: O(log n)
Extraction: O(log n)
Peek: O(1)
Heap operations are efficient because the height of the heap is logarithmic with respect to the number of elements (n) in the heap.

Heaps are widely used in various algorithms and applications, including sorting algorithms like heapsort, graph algorithms like Dijkstra's algorithm, and priority queue implementations. The heapq module in Python provides a convenient way to work with heaps.
    
"""

import heapq as hp
 
l1=[1,4,2,3,7,3,5]
l2=hp.heapify(l1)
print(l1)

hp.heappush(l1,6)
print(l1)
hp.heappop(l1)
print(l1)

