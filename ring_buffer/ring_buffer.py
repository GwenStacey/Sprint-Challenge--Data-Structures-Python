class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.length = 0
        self.cur_ind = 0

    def append(self, item):
        if self.length == self.capacity:
            self.storage[self.cur_ind] = item
            if self.cur_ind < self.capacity-1:
                self.cur_ind+=1
            else:
                self.cur_ind=0
        else:
            self.storage.append(item)
            self.length+=1

    def get(self):
        return self.storage