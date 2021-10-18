from optilog.formulas.modelling import *
from optilog.formulas import CNF
from optilog.sat import Glucose41
from sudoku_base import read_sudoku, var, visualize
import sys


def at_most_one(lits):
    # - YOUR CODE HERE -
    return clauses

def at_least_one(lits):
    # - YOUR CODE HERE -
    return clauses

def exactly_one(lits):
    # - YOUR CODE HERE -
    return clauses

def solve(path):
    cnf = CNF()
    sudoku = read_sudoku(path)
    SUBGROUP_LENGTH = sudoku.subgroup_length
    SUBGROUP_HEIGHT = sudoku.subgroup_height
    VALUES = (SUBGROUP_HEIGHT *  SUBGROUP_LENGTH)

    # ---- Variables ---

    # We have a Boolean for each cell i,j and value v.
    # Function var(i,j,v) returns Boolean variable Bool('Cell_%d_%d_%d'.format(i, j, v))
    #
    # Ex: A call to var(1,1,2) returns Bool('Cell_1_1_2')
    # The intended meaning is: 
    # Cell_1_1_2 is True iff Cell 1,1 is assigned to value 2.
    

    # --- Clauses ----

    # Fixed: Fixed values must appear in their corresponding cell.
    for j in range(VALUES):
        for i in range(VALUES):
            v = sudoku.cells[j][i]
            if v is not None:
                # - YOUR CODE HERE - 

    # Cells: Each Cell contains exactly one value.
    # - YOUR CODE HERE -


    # Row: Each value appears exactly once in each row.
    # - YOUR CODE HERE -


    # Column: Each value appears exactly once in each column.
    # - YOUR CODE HERE -


    # Subgroup: Each value appears exactly once in each subgroup.
    # - YOUR CODE HERE -


    s = Glucose41()
    s.add_clauses(cnf.clauses)
    has_solution = s.solve()
    print('Has solution?', has_solution)

    if has_solution:
        interp = s.model()
        visualize(cnf.decode_dimacs(interp), sudoku)

if __name__ == '__main__':
    solve(sys.argv[1])
