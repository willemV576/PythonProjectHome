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
                current = current.next  # end of the list
            current.prev.next = None  # delete the pointer to the last Node in new last Node
            current.prev = None  # delete the prev pointer in last Node

    def delete_node_key(self, key):
        if self.head is None:
            return
        if self.head.data == key:  # the head is the one to delete
            if self.head.next is None:  # there is only the head
                self.head = None
                # self.tail = None
                return
            else:
                self.head = self.head.next  # make the next Node the Head
                self.head.prev = None  # Set the old head to none
                return
        else:
            current = self.head
            while current is not None:
                if current.data == key:
                    if current.next is None:  # it is the tail to be removed:
                        current.prev.next = None  # set the next.pointer to the tail to None
                        current.prev = None  # set the prev.pointer on the tail to None
                        return
                    else:  # node is in the Middle
                        current.prev.next = current.next
                        current.next.prev = current.prev
                current = current.next

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
    llist.append(5)
    llist.append(6)
    llist.append(7)
    llist.append(8)
    llist.display()
    llist.delete_first_node()
    llist.display()
    llist.delete_last_node()
    llist.display()
    llist.append(6)
    llist.delete_node_key(5)
    llist.display()

if __name__ == "__main__":
    main()
