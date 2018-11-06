[![Functional?](https://img.shields.io/badge/Functional%3F-no-red.svg)](https://shields.io/)

# Solving the 8-puzzles problem
Solving the 8-puzzles problem with best first search, an graph algorithm.

## The 8-puzzles problem
"The 8-puzzle is a smaller version of the slightly better known 15-puzzle. The puzzle consists of an area divided into a
grid, 3 by 3 for the 8-puzzle, 4 by 4 for the 15-puzzle. On each grid square is a tile, expect for one square which remains
empty. Thus, there are eight tiles in the 8-puzzle and 15 tiles in the 15-puzzle. A tile that is next to the empty grid square
can be moved into the empty space, leaving its previous position empty in turn. Tiles are numbered, 1 thru 8 for the 8-puzzle,
so that each tile can be uniquely identified.
The aim of the puzzle is to achieve a given configuration of tiles from a given (different) configuration by sliding the
individual tiles around the grid as described above."
- Reference: http://www.aiai.ed.ac.uk/~gwickler/eightpuzzle-inf.html

## Solving the problem with grapgh algorithm
I solved the problem with an graph algorithm, the best first search. The algorithm is programmed in python.

## Solving the problem with heuristics
We can assume following heuristics:

- h1(n) = number ob misplaced tiles
- h2(n) = sum of manhatten distances of misplaced tiles

I solved the problem with the h1(n).

Further we introduce a new function, to detect the optimal next solution base to continue. 

f(n) = Estimate of optimum cost of solution paths for S that extend the backpointer path of n.

f(n) = length of backpointer path of n + h1(n)

(You can do the same with h2(n))

### Tie breaking
If two or more Nodes in OPEN has the same f(n) value, a tie breaking must decide which node next:

- Go for goal nodes first (Solution found)
- Go for nodes width min h1(n) values
- Latest generated node first

## Inputs
Inputs for the BF() function

- A starting Node 's' as an instance of 'Node"

- A target board configuration as an array. \
target_board_configuration = \
        [ \
            &nbsp;&nbsp;&nbsp;[1, 2, 3], \
            &nbsp;&nbsp;&nbsp;[8, 0, 4], \
            &nbsp;&nbsp;&nbsp;[7, 6, 5] \
]

### Usage
BF(s, target_board_configuration)