import numpy as np

class FibonacciHeap:
    def __init__(self):
        self.nodes = []
        self.min_node_index = -1

    def insert(self, value):
        self.nodes.append(value)
        if self.min_node_index == -1 or value < self.nodes[self.min_node_index]:
            self.min_node_index = len(self.nodes) - 1

    def delete_min(self):
        if self.min_node_index == -1:
            return None
        min_value = self.nodes[self.min_node_index]
        self.nodes.pop(self.min_node_index)
        if not self.nodes:
            self.min_node_index = -1
        else:
            self.min_node_index = np.argmin(self.nodes)

    def replace(self, old_value, new_value):
        if old_value in self.nodes:
            index = self.nodes.index(old_value)
            self.nodes[index] = new_value
            if new_value < self.nodes[self.min_node_index]:
                self.min_node_index = index
            else:
                self.min_node_index = np.argmin(self.nodes)

    def get_number_of_root_nodes(self):
        return len(self.nodes)

# Input handling
num_operations = int(input())
fheap = FibonacciHeap()

for _ in range(num_operations):
    operation = input().split()
    if operation[0] == 'I':
        value = int(operation[1])
        fheap.insert(value)
    elif operation[0] == 'D':
        fheap.delete_min()
    elif operation[0] == 'R':
        old_value = int(operation[1])
        new_value = int(operation[2])
        fheap.replace(old_value, new_value)

# Output the number of root nodes
print(fheap.get_number_of_root_nodes())
