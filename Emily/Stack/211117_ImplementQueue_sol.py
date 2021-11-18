class MyQueue(object):

    def __init__(self):
        self.stack=[]
        self.index=0 # for empty(self) since the element is not deleted
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        return self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.index+=1 
        return self.stack[self.index-1]

    def peek(self):
        """
        :rtype: int
        """
        #self.index+=1
        return self.stack[self.index]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack)-self.index==0
