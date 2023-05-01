from node import Node


class Stack:
    def __init__(self, name, limit=1000):
        self.top_item = None
        self.size = 0
        self.name = name
        self.limit = limit

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            # Increment stack size by 1 here:
            self.size += 1
        else:
            print("Stack is full.")

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            # Decrement the stack size here:
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("Stack is empty.")

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("Stack is empty.")

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

    def print_items(self):
        pointer = self.top_item
        print_list = []
        while pointer:
            print_list.append(pointer.get_value())
            pointer = pointer.get_next_node()

        print_list.reverse()
        print("{} Stack: {}".format(self.get_name(), print_list))


# Driver Code
# Defining an empty pizza stack
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

# Uncomment the push() statement below:
pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

# Uncomment the pop() statement below:
pizza_stack.pop()
