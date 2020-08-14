# Design an Iterator class, which has:
#	 A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
#	 A function next() that returns the next combination of length combinationLength in lexicographical order.
#  A function hasNext() that returns True if and only if there exists a next combination.

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        '''
        :type characters: str
        :type combinationLength: int
        '''

        self.a = itertools.combinations(characters, combinationLength)
        self.b = [''.join(i) for i in self.a]
        self.count = 0

    def next(self) -> str:
        combination = self.b[self.count]
        self.count+=1
        return combination

    def hasNext(self) -> bool:
        return (self.count < len(self.b))


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
