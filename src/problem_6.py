class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    set_1 = make_set(llist_1)
    set_2 = make_set(llist_2)
    union_set = set_1.union(set_2)
    result = LinkedList()
    for element in union_set:
        result.append(element)
    return result

def intersection(llist_1, llist_2):
    # Your Solution Here
    set_1 = make_set(llist_1)
    set_2 = make_set(llist_2)
    intersection_set = set_1.intersection(set_2)
    result = LinkedList()
    for element in intersection_set:
        result.append(element)
    return result

def make_set(llist):
    result = set()
    node = llist.head
    while node:
        result.add(node.value)
        node = node.next
    return result

def eval_test(test_number, expected_output, actual_output):
    print("")
    print("TEST CASE " + str(test_number))
    print("===========")
    print("- expected output (order of elements may differ):")
    print(expected_output)
    print("- actual output:")
    print(actual_output)
    print("")

if __name__ == "__main__":
    # test case 1
    llist_1 = LinkedList()
    llist_2 = LinkedList()
    result = union(llist_1, llist_2)
    expected_output = ""
    eval_test(1, expected_output, result)

    # test case 2
    result = intersection(llist_1, llist_2)
    expected_output = ""
    eval_test(2, expected_output, result)

    # test case 3
    llist_1 = LinkedList()
    llist_2 = LinkedList()
    element_1 = [3,2,4,35,6,65,6,4,3,21]
    for e in element_1:
        llist_1.append(e)
    element_2 = [6,32,4,9,6,1,11,21,1]
    for e in element_2:
        llist_2.append(e)
    result = union(llist_1, llist_2)
    expected_output = "32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->"
    eval_test(3, expected_output, result)

    # test case 4
    result = intersection(llist_1, llist_2)
    expected_output = "4 -> 21 -> 6 ->"
    eval_test(4, expected_output, result)

    # test case 5
    llist_1 = LinkedList()
    llist_2 = LinkedList()
    element_1 = [3,2,4,35,6,65,6,4,3,21]
    for e in element_1:
        llist_1.append(e)
    result = union(llist_1, llist_2)
    expected_output = "65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 21 ->"
    eval_test(5, expected_output, result)

    # test case 6
    result = intersection(llist_1, llist_2)
    expected_output = ""
    eval_test(6, expected_output, result)

    # test case 7
    llist_1 = LinkedList()
    llist_2 = LinkedList()
    element_2 = [6,32,4,9,6,1,11,21,1]
    for e in element_2:
        llist_2.append(e)
    result = union(llist_1, llist_2)
    expected_output = "32 -> 1 -> 4 -> 21 -> 6 -> 9 -> 11 ->"
    eval_test(7, expected_output, result)

    # test case 8
    result = intersection(llist_1, llist_2)
    expected_output = ""
    eval_test(8, expected_output, result)

"""
# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
"""