import sys
import clingo

def sorted_atoms(model):
    return sorted(str(s) for s in model.symbols(shown=True))

class Solver(clingo.application.Application):
    program_name = "sudoku-solver"
    version = "1.0"

    def print_model(self, model, printer):
        print(" ".join(sorted_atoms(model)))

    def load_files(self, ctl, files):
        for f in (files if files else ["-"]):
            ctl.load(f)

    def main(self, ctl, files):
        ctl.load("sudoku.lp")
        self.load_files(ctl, files)
        ctl.ground([("base", [])])
        return ctl.solve()

def run():
    clingo.application.clingo_main(Solver(), sys.argv[1:])

if __name__ == "__main__":
    run()