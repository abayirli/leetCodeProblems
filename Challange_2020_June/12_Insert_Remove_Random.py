# LeedCode June Challange Day 12
# Insert Delete GetRandom O(1) Problem

# Design a data structure that supports all following operations in average O(1) time.

#     insert(val): Inserts an item val to the set if not already present.
#     remove(val): Removes an item val from the set if present.
#     getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.


import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.hashmap = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if(val not in self.array):
            index = len(self.array)
            self.array.append(val)
            self.hashmap[val] = index
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if(val in self.array):
            index = self.hashmap[val]
            last_element = self.array[-1]
            self.array[index] = last_element
            self.hashmap[last_element] = index
            del self.hashmap[val]
            self.array.pop()
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.array)