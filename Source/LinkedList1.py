class Node:
    def __init__(self, data=None):
        self.data = data  # Initialise the node with data
        self.pointer_next = None  # Initialise the next pointer to None
        self.pointer_prev = None  # Initialise the previous pointer to None

    def __str__(self):
        # Printing attributes of the Node get the data of the next and previous nodes, or None if they don't exist
        next_data = self.pointer_next.data if self.pointer_next else None
        prev_data = self.pointer_prev.data if self.pointer_prev else None
        return f"Node(data: {self.data}, next_data: {next_data}, prev_data: {prev_data}, address: {id(self)})"

class LinkedList:
    def __init__(self):
        self.head = None  # Initialise the head of the list to None

    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:  # If the list is empty
            self.head = new_node  # Set the new node as the head
            print("self.head set to new_node")
            return
        find_last_node = self.head  # Start from the head of the list
        while find_last_node.pointer_next:  # Loop to the end of the list
            find_last_node = find_last_node.pointer_next
        find_last_node.pointer_next = new_node
        new_node.pointer_prev = find_last_node
        new_node.pointer_next = None

    def remove(self, data):
        #print("Remove method was called with data:", data)
        find_node = self.head
        while find_node:  # Loop to end of the list
            if find_node.data == data:
                print(f"Node to be removed {find_node}")  # This will print found the node
                next_data = find_node.pointer_next
                prev_data = find_node.pointer_prev
                print(f"next_data {next_data}")
                print(f"prev_data {prev_data}")

                prev_node =  self.head
                while prev_node:
                    ...


            find_node = find_node.pointer_next  # Move to next node

    def print_list(self): # Print list of all nodes
        current_node = self.head
        while current_node:
            print(current_node)
            current_node = current_node.pointer_next

# Example usage:
llist = LinkedList()  # Create a new linked list
llist.append(1)  # Append 1 to the list
llist.append(2)  # Append 2 to the list
llist.append(3)  # Append 3 to the list
llist.append(4)  # Append 3 to the list
llist.append(5)  # Append 3 to the list
llist.remove(4)  # Append 3 to the list
#llist.print_list()  # Print the list