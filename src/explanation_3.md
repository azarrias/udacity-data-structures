# Problem 3: Huffman Coding
## Time complexity
I chose to implement the priority queue using a min-heap, because its insertion operation has a worst-case time complexity of O(log n) but an average-case complexity of O(1), which is good for this problem. We need to traverse the tree for encoding and decoding the input string, which are O(n) complexity operations.
Anyway, since we need to insert all elements while creating the tree, we must consider a worst-case time complexity of O(n log n) for this solution.
## Space complexity
Space complexity is linear O(n), since all the data that we need to store depends on the characters on the input string.