def quick_sort(orders):
    if len(orders) <= 1:
        return orders
    pivot = orders[0]
    lesser = [order for order in orders[1:] if order[1] < pivot[1]]
    greater = [order for order in orders[1:] if order[1] >= pivot[1]]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

# Example Usage
orders = [(101, 3), (102, 1), (103, 2)]  # (Order ID, Priority)
sorted_orders = quick_sort(orders)
print("Sorted Orders by Priority:", sorted_orders)
