class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


    def data_insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.data_insert(data)

            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.data_insert(data)
   
        else:
            self.data = data
