from dataclasses import dataclass
import random
from typing import List


@dataclass
class Individual:
    # List where the positions of the number inside the list represnets
    # the column and the number itself represents the row where the queen is.
    # e.g. queens[0] = 1 represents a queen in the first column at the second row
    queens: List[int]

    def pprint(self):
        queen = '♛'
        nothing = '·'
        n = len(self.queens)
        for row in range(n):
            for col in range(n):
                elem = self.queens[col]
                if elem == row:
                    print(f"{queen} ", end='')
                else:
                    print(f"{nothing} ", end='')
            print()

    @classmethod
    def new_random(cls, n: int = 8) -> "Individual":
        queens = [random.randint(0, n) for _ in range(n)]
        return Individual(queens=queens)


if __name__ == '__main__':
    individual = Individual.new_random()
    individual.pprint()
