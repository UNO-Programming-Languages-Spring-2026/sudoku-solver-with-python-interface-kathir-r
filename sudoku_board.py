from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE
        for i in range(1, 10):
            cells = []
            for j in range(1, 10):
                cells.append(str(self.sudoku[(i, j)]))

            group1 = " ".join(cells[0:3])
            group2 = " ".join(cells[3:6])
            group3 = " ".join(cells[6:9])
    
            s += "  ".join([group1, group2, group3])
    
            if i != 9:
                s += "\n"
            if i in (3, 6):
                s += "\n"
        
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        row = 1
        for line in s.splitlines():
            if not line.strip():
                continue
            col = 1
            for val in line.split():
                if val != "-":
                    sudoku[row, col] = int(val)
                col += 1
            row += 1
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        for a in model.symbols(shown=True):
             r, c, v = (x.number for x in a.arguments)
             sudoku[(r, c)] = v
        return cls(sudoku)
