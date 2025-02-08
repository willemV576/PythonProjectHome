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
        find_last_node.pointer_next = new_node #set the new node as the pointer_next of the last_node
        new_node.pointer_prev = find_last_node #set the last node as the pointer_prev of new node
        new_node.pointer_next = None #set pointer_prev of new node to None, because it is the tail

    def insert_at_start(self, data):
        if self.head is None:
            print("The List is empty")
            return
        new_node = Node(data) # create new Node
        new_node.pointer_next = self.head # Set the object of pointer_next of the new node to the head, the head comes now after the new node
        self.head.pointer_prev = new_node # set the pointer_prev object of the head to the new node, the head points now back to the new node
        self.head = new_node # make the new node the head

    def reverse(self):
        if self.head is None: # you can't reverse nothing
            print("The List is empty")
            return

        find_node = self.head # Start from the head of the list
        prev_node = None
        while find_node: # Loop to end of the list
            next_node = find_node.pointer_next # store object in pointer_next before changed in the next line
            find_node.pointer_next = find_node.pointer_prev # give pointer_next the object of find_node.pointer_prev
            find_node.pointer_prev = next_node # assign stored object in pointer_next to pointer_prev

            prev_node = find_node
            find_node = next_node

        self.head = prev_node # the last remaining loop value of prev_node is the new head
        print(f"find_node val {find_node}")

    def insert_in_location(self, data):
        ...

    def remove(self, data):
        find_node = self.head # Start from the head of the list
        while find_node:  # Loop to end of the list
            if find_node.data == data:
                print(f"Node to be removed {find_node}")  # This will print found the node
                next_data = find_node.pointer_next
                prev_data = find_node.pointer_prev
                print(f"next_data {next_data}") # This will print value of date for the found node
                print(f"prev_data {prev_data}")

                #prev_node = self.head  # Start from the head of the list
                #while prev_node:
                #    if find_node.
                #    prev_node = prev_node.pointer_next # Move to next prev_node

            find_node = find_node.pointer_next  # Move to next find_node

    def print_list(self):  # Print list of all nodes
        find_node = self.head
        while find_node:
            print(find_node)
            find_node = find_node.pointer_next


def main():
    # Example usage:
    llist = LinkedList()  # Create a new linked list
    llist.append(1)  # Append 1 to the list
    llist.append(2)  # Append 2 to the list
    llist.append(3)  # Append 3 to the list
    llist.append(4)  # Append 3 to the list
    llist.append(5)  # Append 3 to the list
    #llist.remove(3)  # Append 3 to the list
    llist.insert_at_start(66)
    ##llist.print_list()  # Print the list
    ##print("---+++---")
    llist.reverse()
    ##llist.print_list()  # Print the list
    ##print("---+++---")
    llist.insert_at_start(99)
    llist.print_list()
    print("---+++---")


if __name__  == "__main__":
    main()
