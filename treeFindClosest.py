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
            
    def searchVal(self, data):
        if data < self.data:
            if self.left is None:
                return str(data)+" is not Found in the Binary Tree"

            return self.left.searchVal(data)
        elif data > self.data:
            if self.right is None:
                return str(data)+" is not Found in the Binary Tree"
            return self.right.searchVal(data)
        else:
            return str(self.data) + " is found in the Binary Tree"
        
def calculate_branch_sum(node, running_sum, sums):
    if node is None:
        return

    new_running_sum = running_sum + node.data

    if node.left is None and node.right is None:
        sums.append(new_running_sum)
        return

    calculate_branch_sum(node.left, new_running_sum, sums)
    calculate_branch_sum(node.right, new_running_sum, sums)
