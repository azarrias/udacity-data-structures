import hashlib
import datetime

class Block:
    def __init__(self, ident, data, previous_hash):
        self.id = ident
        self.timestamp = str(datetime.datetime.utcnow())
        self.data = data
        self.previous_hash = previous_hash
        self.previous = None
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        sha.update(self.timestamp.encode('utf-8'))
        return sha.hexdigest()

class BlockChain:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def __str__(self):
        if self.head is None:
            return "BlockChain is empty"
        node = self.head
        result = ""
        while node:
            result += "\nBlock " + str(node.id) + "\nTimestamp: " + node.timestamp + "\nData: " + node.data \
                + "\nSHA256 Hash: " + str(node.hash) + "\nPrev_Hash: " + str(node.previous_hash) + "\n"
            node = node.previous
        return result[1:]

    def size(self):
        return self.num_elements

    def prepend(self, data):
        # prepend a value to the beggining of the linked list
        self.num_elements += 1
        if self.head is None:
            self.head = Block(self.size() - 1, data, 0)
        else:
            block = Block(self.size() - 1, data, self.head.hash)
            block.previous = self.head
            self.head = block

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
    # expected output: "BlockChain is empty"
    blockchain = BlockChain()
    eval_test(1, "BlockChain is empty", blockchain)

    # test case 2
    # expected output: blockchain displays properly with correct hash links between blocks
    blockchain2 = BlockChain()
    blockchain2.prepend("Some data")
    blockchain2.prepend("More data")
    blockchain2.prepend("Even more data")
    expected_output = "BlockChain displays data properly, including correct hash links between blocks"
    eval_test(2, expected_output, blockchain2)

    # test case 3
    # expected output: blockchain displays properly with correct hash links between blocks
    blockchain3 = BlockChain()
    blockchain3.prepend("")
    blockchain3.prepend("Not empty")
    blockchain3.prepend("Also not empty")
    expected_output = "BlockChain displays data properly, including correct hash links between blocks"
    eval_test(2, expected_output, blockchain3)