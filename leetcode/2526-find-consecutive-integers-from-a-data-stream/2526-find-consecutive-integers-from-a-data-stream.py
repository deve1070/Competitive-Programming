from collections import deque
class DataStream:

    def __init__(self, value: int, k: int):
        self.stream=deque()
        self.k=k
        self.value=value
        

    def consec(self, num: int) -> bool:
        if num ==self.value:
            self.stream.append(num)
        else:
            self.stream.clear()
        if len(self.stream) > self.k:
            self.stream.popleft()
        
        return len(self.stream)==self.k
       
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)