class Node:
    def __init__(self, data=None):
        self.data = data  # Initialize the node with data
        self.pointer = None  # Initialize the next pointer to None

    def __str__(self):
        pointer_data = self.pointer.data if self.pointer else None
        return f"Node(data: {self.data}, pointer: {pointer_data})"


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list to None

    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data

        if not self.head:  # If the list is empty
            self.head = new_node  # Set the new node as the head
            print("self.head set to new_node")
            return
        last_node = self.head  # Start from the head of the list
        print(f"last node1: {last_node}")

        while last_node.pointer:  # Traverse to the end of the list
            last_node = last_node.pointer
            print(f"last node2: {last_node}")
        last_node.pointer = new_node  # Set the next of the last node to the new node
        print(f"last node2: {last_node}")

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node)
            current_node = current_node.pointer



# Example usage:
llist = LinkedList()  # Create a new linked list
llist.append(1)  # Append 1 to the list
llist.append(2)  # Append 2 to the list
#llist.append(3)  # Append 3 to the list
#llist.append(4)  # Append 3 to the list
#llist.append(5)  # Append 3 to the list

#llist.print_list()  # Print the list