class Node:
    def __init__(self, order_id, details):
        self.order_id = order_id
        self.details = details
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_order(self, order_id, details):
        new_node = Node(order_id, details)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def process_orders(self):
        current = self.head
        while current:
            print(f"Processing Order ID: {current.order_id}, Details: {current.details}")
            current = current.next

# Example Usage
orders = DoublyLinkedList()
orders.add_order(101, "Order A")
orders.add_order(102, "Order B")
orders.add_order(103, "Order C")

orders.process_orders()
