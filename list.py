class Node:
    """A class to represent a node in the doubly linked list."""

    def __init__(self, value):
        self.value = value  # Data stored in the node
        self.next = None    # Pointer to the next node
        self.prev = None    # Pointer to the previous node


class DoublyLinkedList:
    """A class to represent a doubly linked list."""

    def __init__(self):
        self.head = None  # The first node in the list
        self.tail = None  # The last node in the list
        self.size = 0     # Number of nodes in the list

    def append(self, value):
        """Add a node to the end of the list."""
        new_node = Node(value)
        if not self.head:
            # If the list is empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Link the new node to the current tail
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def prepend(self, value):
        """Add a node to the beginning of the list."""
        new_node = Node(value)
        if not self.head:
            # If the list is empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Link the new node to the current head
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def remove(self, value):
        """Remove the first node with the given value."""
        if not self.head:
            return  # The list is empty

        current = self.head
        while current:
            if current.value == value:
                # If the node is the head
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                # If the node is the tail
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    # Update pointers to skip over the current node
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.size -= 1
                return
            current = current.next

    def print_forward(self):
        """Print the list from head to tail."""
        current = self.head
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def print_backward(self):
        """Print the list from tail to head."""
        current = self.tail
        elements = []
        while current:
            elements.append(current.value)
            current = current.prev
        print(" <- ".join(map(str, elements)))

    def get_size(self):
        """Return the number of nodes in the list."""
        return self.size


# Example Usage
dll = DoublyLinkedList()

# Append nodes
dll.append(10)
dll.append(20)
dll.append(30)

# Prepend nodes
dll.prepend(5)

# Print list forward and backward
dll.print_forward()  # Output: 5 -> 10 -> 20 -> 30
dll.print_backward()  # Output: 30 <- 20 <- 10 <- 5

# Remove a node
dll.remove(20)
dll.print_forward()  # Output: 5 -> 10 -> 30

# Check size
print("Size of list:", dll.get_size())  # Output: Size of list: 3