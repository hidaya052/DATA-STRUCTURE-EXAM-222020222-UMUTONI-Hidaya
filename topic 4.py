class Node:
    def __init__(self, order_id, details):
        self.order_id = order_id
        self.details = details
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_order(self, order_id, details):
        new_node = Node(order_id, details)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display_orders(self):
        current = self.head
        while current:
            print(f"Order ID: {current.order_id}, Details: {current.details}")
            current = current.next

# Example Usage
orders = SinglyLinkedList()
orders.add_order(201, "Order X")
orders.add_order(202, "Order Y")
orders.add_order(203, "Order Z")

orders.display_orders()
