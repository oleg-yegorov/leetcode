from random import choice


class RandomizedSet:
    def __init__(self):
        self.l = []

    def insert(self, val: int) -> bool:
        r = not (val in self.l)
        self.l.append(val)
        return r

    def remove(self, val: int) -> bool:
        r = val in self.l
        if r:
            index = self.l.index(val)
            self.l[index], self.l[len(self.l) - 1] = self.l[len(self.l) - 1], self.l[index]
            self.l.pop()
        return r

    def getRandom(self) -> int:
        return choice(self.l)
