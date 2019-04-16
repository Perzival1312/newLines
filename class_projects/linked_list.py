class Node(object):
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None  # an OBJECT
        self.prev = None  # an OBJECT

    def __repr__(self):
        """Return a string representation of this node."""
        return "Node({!r})".format(self.data)


class LListIter(object):
    def __init__(self, item):
        self.item = item

    def __next__(self):
        node = self.item
        if node == None:
            raise StopIteration
        self.item = self.item.next
        return node


class LinkedList(object):
    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0
        # Append given items
        if items is not None:
            for ind, item in enumerate(items):
                new_node = Node(item)
                if ind - 1 >= 0:
                    prev_node = Node(items[ind - 1])
                    new_node.prev = prev_node
                else:
                    new_node.prev = None
                try:
                    next_node = Node(items[ind + 1])
                    new_node.next = next_node
                except:
                    pass
                self.append(new_node)
                if self.head is None:
                    self.head = new_node
            self.tail = new_node

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ["({!r})".format(item) for item in self.items()]
        return "[{}]".format(" -> ".join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return "LinkedList({!r})".format(self.items())

    def __iter__(self):
        return LListIter(self.head)

    def __getitem__(self, ind):
        node = self.head
        for _ in range(ind - 1):
            node = node.next
        return node

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        # O(1)
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?
                searching through all nodes"""
        # TODO: Loop through all nodes and count one for each
        return self.size

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Why and under what conditions?
                just changes some values"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        if type(item) != Node:
            new_node = Node(item)
        else:
            new_node = item
        if self.tail is not None:
            new_node.prev = self.tail
            self.tail.next = new_node
        if self.head is None:
            self.head = new_node
        self.tail = new_node
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) Why and under what conditions?
                just changes some values"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        if type(item) != Node:
            new_node = Node(item)
        else:
            new_node = item
        if self.head is not None:
            temp_node = self.head
            temp_node.prev = new_node
            new_node.next = self.head
        else:
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(1) Why and under what conditions?
                quality is head only chacking once
        TODO: Worst case running time: O(n) Why and under what conditions?
                quality is tail checking entire list                     """
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        node = self.head  # gets first element in linked list
        while node is not None:  # checks to see if it is a node
            if quality(
                node.data
            ):  # runs quality func which chacks if node data is equal to func input
                return node.data  # if true returning nodes data
            node = node.next  # next node
        return None  # default if not found

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) Why and under what conditions?
                item is head therefore only chcking once
        TODO: Worst case running time: O(n) Why and under what conditions?
                item is tail chcking entire ll"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        node = self.head
        try:
            prev_node = node.prev
        except:
            prev_node = None
        while node is not None:
            if node.data == item:
                try:
                    prev_node.next = node.next
                except:
                    pass
                if node == self.head:
                    self.head = node.next
                    try:
                        self.head.prev = None
                    except:
                        pass
                try:
                    if node.data == self.tail.data:
                        self.tail = prev_node
                except:
                    pass
                node.next = None
                self.size -= 1
                break
            prev_node = node
            node = node.next
        else:
            raise ValueError("Item not found: {}".format(item))

    def replace(self, old, new):
        node = self.head
        while node is not None:
            if node.data == old:
                node.data = new
                break
            node = node.next
        else:
            raise ValueError("Item not found: {}".format(old))


def test_linked_list():
    ll = LinkedList(["A", "B", "C"])
    print("list: {}".format(ll))

    print("\nTesting append:")
    for item in ["D", "E", "F"]:
        print("append({!r})".format(item))
        ll.append(item)
        print("list: {}".format(ll))

    print("head: {}".format(ll.head))
    print("tail: {}".format(ll.tail))
    print("length: {}".format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print("\nTesting delete:")
        for item in ["B", "C", "A"]:
            print("delete({!r})".format(item))
            ll.delete(item)
            print("list: {}".format(ll))

        print("head: {}".format(ll.head))
        print("tail: {}".format(ll.tail))
        print("length: {}".format(ll.length()))

    ll.replace("D", "G")
    # for items in ll:
    #     for item in ll:
    #         print(item, items)
    print(ll[6])
    # print(item)
    # print(ll)


if __name__ == "__main__":
    test_linked_list()
