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
