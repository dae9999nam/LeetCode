class MyStack(object):

    def __init__(self):
        self.q1 = [] # initial queue
        self.q2 = []
        self.length = len(self.q1)

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.append(x)
        self.length = len(self.q1)


    def pop(self):
        """
        :rtype: int
        """
        while self.length > 1:
            # until the last element left
            temp = self.q1.pop(0)
            self.length = len(self.q1)
            self.q2.append(temp)

        target = self.q1.pop(0)
        self.q1 = self.q2
        self.q2 = []
        self.length = len(self.q1)
        return target


    def top(self):
        """
        :rtype: int
        """
        while self.length > 1:
            temp = self.q1.pop(0)
            self.length = len(self.q1)
            self.q2.append(temp)

        target = self.q1.pop(0)
        self.q2.append(target)
        self.q1 = self.q2
        self.q2 = []
        self.length = len(self.q1)
        return target

    def empty(self):
        """
        :rtype: bool
        """
        # return self.length
        if self.length > 0:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()