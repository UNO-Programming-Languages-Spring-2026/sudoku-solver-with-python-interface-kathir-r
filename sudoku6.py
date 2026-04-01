import clingo
from sudoku_board import Sudoku


class Context:

    def __init__(self, board: Sudoku):
        self.board = board

    def initial(self) -> list[clingo.symbol.Symbol]:
        symbols = []
        for position, value in self.board.sudoku.items():
            row = position[0]
            col = position[1]
            args = [clingo.Number(row), clingo.Number(col), clingo.Number(value)]
            symbols.append(clingo.symbol.Function("", args))
        return symbols
    
class SudokuSolver(clingo.application.Application):
    program_name = "sudoku-solver"
    version = "1.0"

    def build_grid(self, model):
        grid = {}
        for a in model.symbols(shown=True):
            r, c, v = (x.number for x in a.arguments)
            grid[(r, c)] = v
        return grid

    def format_grid(self, grid):
        s = ""
        for i in range(1, 10):
            cells = []
            for j in range(1, 10):
                cells.append(str(grid[(i, j)]))

            group1 = " ".join(cells[0:3])
            group2 = " ".join(cells[3:6])
            group3 = " ".join(cells[6:9])

            s += "  ".join([group1, group2, group3])

            if i != 9:
                s += "\n"
            if i in (3, 6):
                s += "\n"
        return s

    def print_model(self, model, printer):
        grid = self.build_grid(model)
        print(self.format_grid(grid))

    def main(self, ctl, files):
        ctl.load("sudoku.lp")
        for f in (files if files else ["-"]):
            ctl.load(f)
        ctl.ground([("base", [])])
        return ctl.solve()

def run():
    clingo.application.clingo_main(SudokuSolver(), sys.argv[1:])

if __name__ == "__main__":
    run()
