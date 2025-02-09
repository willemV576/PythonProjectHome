from distutils.dep_util import newer


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail = None

    def append(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new
            new.prev = current

    def delete_first_node(self):
        if self.head is None:  # if list is empty
            return
        if self.head.next is None:  # there is only the head
            self.head = None
            return
        else:
            old = self.head  # store the old head
            self.head = self.head.next  # make the next of the head the new head
            self.head.prev = None  # remove the prev of the head
            old.next = None  # clean up

    def delete_last_node(self):
        if self.head is None:  # if list is empty
            return
        if self.head.next is None:  # there is only the head
            self.head = None
            return
        else:
            current = self.head
            while current.next:
                current = current.next # end of the list
            current.prev.next = None # delete the pointer to the last Node in new last Node
            current.prev = None # delete the prev pointer in last Node


    def display(self):
        current = self.head
        while current.next:
            print(current.data, end="<-->")
            current = current.next
        print(None)


def main():
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.display()
   # llist.delete_first_node()
   # llist.display()
    llist.delete_last_node()
    llist.display()

if __name__ == "__main__":
    main()
