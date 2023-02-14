from multiprocessing.sharedctypes import Value


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.rifgt = None

    def branchSums(self):
        sums = []
        calculateBranchsums(self, 0, sums)
        return sums
    
def calculateBranchsums(self, runningSum, sums):
    if self.value is None:
        return
    newRunningSum = runningSum + self.value
    if self.left is None and self.right is None:
        sums.append(newRunningSum)
        return 
