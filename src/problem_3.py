import sys
from collections import Counter
import heapq

class HuffmanNode(object):
    def __init__(self, left=None, right=None, root=None):
        self.left = left
        self.right = right
        self.root = root
    def __lt__(self,other):
        return False
    __gt__ = __lt__

def build_huffman_tree(string):
    frequencies = Counter(string)
    # use min-heap for lower time complexity when sorting elements upon insertion
    min_heap = []
    for character, frequency in frequencies.items():
        heapq.heappush(min_heap, (frequency, character))
    while len(min_heap) > 1:
        l, r = heapq.heappop(min_heap), heapq.heappop(min_heap)
        node = HuffmanNode(l, r)
        heapq.heappush(min_heap, (l[0] + r[0], node))
    return heapq.heappop(min_heap)

def get_huffman_codes(node, prefix = ''):
    # base case: it is not an internal huffman node, but a leaf
    if not isinstance(node, HuffmanNode):
        return { node : prefix }

    # recursively add 0 to left child and 1 to right child nodes
    dictl = get_huffman_codes(node.left[1], prefix + '0')
    dictr = get_huffman_codes(node.right[1], prefix + '1')
    dictl.update(dictr)
    return dictl

def huffman_encoding(data):
    if data is None or len(data) == 0:
        return "", None
    _, tree = build_huffman_tree(data)
    codes = get_huffman_codes(tree)
    encoded = ""
    for character in data:
        encoded += codes[character]
    return encoded, tree

def huffman_decoding(data, tree):
    decoded = ""
    node = tree
    for bit in data:
        if bit == '0':
            node = node.left[1]
        elif bit == '1':
            node = node.right[1]
        # if a leaf node is encountered, append its character to the decoded string
        if not isinstance(node, HuffmanNode):
            decoded += node
            node = tree
    return decoded

def eval_test(test_number, expected_output, actual_output):
    print("")
    print("TEST CASE " + str(test_number))
    print("===========")
    print("- expected output:")
    print(expected_output)
    print("- actual output:")
    print(actual_output)
    print("")

if __name__ == "__main__":
    # test case 1
    input_str = "The bird is the word"
    encoded_data, tree = huffman_encoding(input_str)
    result = huffman_decoding(encoded_data, tree)
    expected_output = "The bird is the word"
    eval_test(1, expected_output, result)

    # test case 2
    input_str = ""
    encoded_data, tree = huffman_encoding(input_str)
    result = huffman_decoding(encoded_data, tree)
    expected_output = ""
    eval_test(2, expected_output, result)

    # test case 3
    input_str = None
    encoded_data, tree = huffman_encoding(input_str)
    result = huffman_decoding(encoded_data, tree)
    expected_output = ""
    eval_test(3, expected_output, result)

    # test case 4
    input_str = "AAAAAAABBBCCCCCCCDDEEEEEEAAAAAAABBBCCCCCCCDDEEEEEEAAAAAAABBBCCCCCCCDDEEEEEEAAAAAAABBBCCCCCCCDDEEEEEEAAAAAAABBBCCCCCCCDDEEEEEEAAAAAAABBBCCCCCCCDDEEEEEE"
    encoded_data, tree = huffman_encoding(input_str)
    result = huffman_decoding(encoded_data, tree)
    expected_output = "AAAAAAABBBCCCCCCCDDEEEEEEAAAAAAABBBCCCCCCCDDEEEEEEAAAAAAABBBCCCCCCCDDEEEEEEAAAAAAABBBCCCCCCCDDEEEEEEAAAAAAABBBCCCCCCCDDEEEEEEAAAAAAABBBCCCCCCCDDEEEEEE"
    eval_test(4, expected_output, result)

"""
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
"""
