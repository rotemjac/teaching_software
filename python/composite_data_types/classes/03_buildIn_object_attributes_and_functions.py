
class Worker:
    pass

# The hasattr function - tells if object has a specific attribute
hasattr(Worker, '__init__') # Prints: True

worker1 = Worker()
hasattr(worker1, '__init__') # Prints: True



# The __dict__ attribute - show all object attributes
class Center:
    def __init__(self, phone):
        self.phone = phone

center1 = Center("123456")
print(center1.__dict__)  # shows all object attributes and the values