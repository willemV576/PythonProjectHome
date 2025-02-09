class Node:
    def __init__(self, data):  # initialise new node
        self.data = data  # attribute to hold value
        self.next = None  # attribute to indicate next Node
        self.prev = None  # attribute to indicate previous Node


class LinkedList:
    def __init__(self):
        self.head = None  # attribute to indicate that the node is the head of the list
        # self.tail = None #attribute to indicate that the node is the tail of the list (to be implemented)

    def append(self, data):  # method to add a node to the end of the list
        new = Node(data)  # construct new node
        if not self.head:  # if there is no head, the now node is the head.
            self.head = new
            return
        else:
            current = self.head  # go to the end of the list where there to the node that has no next
            while current.next:
                current = current.next
            current.next = new  # set the new node as the next of the current (last)node
            new.prev = current  # set the new node as prev the current.

    def insert_at_start(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        else:
            self.head.prev = new  # the set new as the prev of the head
            new.next = self.head  # the set the head as the next of new
            self.head = new  # make new the new head

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print(None)


def main():
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.insert_at_start(55)
    llist.display()


if __name__ == "__main__":
    main()
