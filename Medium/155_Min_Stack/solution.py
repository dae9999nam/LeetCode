class MinStack(object):

    def __init__(self):
        self.arr = []
        self.length = len(self.arr)
        self.sort = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.arr.append(val)
        sort = sorted(self.arr)
        self.sort = sort
        self.length = len(self.arr)

    def pop(self):
        """
        :rtype: None
        """
        self.arr = self.arr[:self.length-1]
        self.length = len(self.arr)
        self.sort = sorted(self.arr)


    def top(self):
        """
        :rtype: int
        """
        return self.arr[self.length-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.sort[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()