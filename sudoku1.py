import clingo
import sys

class SolverApp(clingo.Application):
    def __init__(self):
        super().__init__()
        self.program_name = "sudoku"

    def main(self, ctl, input_files):
        ctl.load("sudoku.lp")

        for file_name in input_files:
            ctl.load(file_name)

        ctl.ground([("base", [])])

        result = ctl.solve()

        return result


def run():
    app = SolverApp()
    clingo.clingo_main(app, sys.argv[1:])


if __name__ == "__main__":
    run()