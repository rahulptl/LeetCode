import random
class RandomizedSet:

    def __init__(self):
        
        self.store = []

    def insert(self, val: int) -> bool:
        if val in self.store:
            return False
        else:
            self.store.append(val)
            return True
    
    def remove(self, val: int) -> bool:
        if val in self.store:
            self.store.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(self.store)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()