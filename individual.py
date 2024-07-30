from dataclasses import dataclass
from typing import List


@dataclass
class Individual:
    # List where the positions of the number inside the list represnets
    # the column and the number itself represents the row where the queen is.
    # e.g. queens[0] = 1 represents a queen in the first column at the second row
    queens: List[int]

    def pprint(self):
        queen = '♕'
        nothing = 'x'
        n = len(self.queens)
        for row in range(n):
            for col in range(n):
                elem = self.queens[col]
                if elem == row:
                    print(f"{queen} ", end='')
                else:
                    print(f"{nothing} ", end='')
            print()
