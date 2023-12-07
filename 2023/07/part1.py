rankings = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")


class Hand:
    def __init__(self, line):
        self.__cards, self.rank = line.split(" ")
        self.rank = int(self.rank)

    def get_type(self):
        if self.__cards.count(self.__cards[0]) == 5:
            return 7
        for char in self.__cards:
            if self.__cards.count(char) == 4:
                return 6
        for char in self.__cards:
            if self.__cards.count(char) == 3:
                if self.__cards.replace(char, "").count(self.__cards.replace(char, "")[0]) == 2:
                    return 5
                return 4
        for char in self.__cards:
            if self.__cards.count(char) == 2:
                for char2 in self.__cards:
                    if self.__cards.count(char2) == 2 and char != char2:
                        return 3
                return 2
        return 1

    def is_bigger(self, other):
        for char1, char2 in zip(self.__cards, other.__cards):
            if char1 != char2:
                return rankings.index(char1) > rankings.index(char2)

    def __lt__(self, other):
        if self.get_type() == other.get_type():
            return not self.is_bigger(other)
        return self.get_type() < other.get_type()


with open("input.txt", "r", encoding="utf-8") as f:
    data = [Hand(s) for s in f.read().splitlines()]

data.sort()
print(sum([(i+1)*v.rank for i, v in enumerate(data)]))