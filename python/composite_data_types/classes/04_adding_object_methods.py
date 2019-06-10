
# The name of the file could also be adding class methods, BUT
# I wanted to emphasize that those are not static methods that only belong to a class
# but a method that will be created for EACH OBJECT

class Center:

    def __init__(self, phone):
        self.phone = phone


    def open(self, message):
        print("Hello! The center will be open, a message: " , message)


center1 = Center("12345")
center1.open("Some message from center1")