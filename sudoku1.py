import clingo
import sys

def load_files(ctl, files):
    for f in files:
        ctl.load(f)

def print_model(model):
    atoms = list(model.symbols(shown=True))
    atoms.sort()
    print("Answer:", model.number)
    print(" ".join(map(str, atoms)))

class SolverApp(clingo.Application):
    def __init__(self):
        super().__init__()
        self.program_name = "sudoku"

    def main(self, ctl, files):
        ctl.load("sudoku.lp")
        load_files(ctl, files)
        ctl.ground([("base", [])])
        ctl.solve(on_model=print_model)

def solve(encoding, inputs):
    app = SolverApp()
    clingo.clingo_main(app, inputs)

if __name__ == "__main__":
    solve("sudoku.lp", sys.argv[1:])