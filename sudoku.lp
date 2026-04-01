% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)

%Q1a
cell(1..9).
value(1..9).

sudoku(X,Y,N) :- initial(X,Y,N).

1 { sudoku(X,Y,N) : value(N) } 1 :- cell(X), cell(Y), not initial(X,Y,_).

:- cell(X), value(N), 2 { sudoku(X,Y,N) : cell(Y) }.

:- cell(Y), value(N), 2 { sudoku(X,Y,N) : cell(X) }.

%Q2, 9x9
n(3).
%using the hint to use a formula based subgrid
subgrid(X,Y,G) :- cell(X), cell(Y), n(N), G = 1 + ((X-1)/N)*N + (Y-1)/N. 

:- G = 1..9, value(N), 2 { sudoku(X,Y,N) : subgrid(X,Y,G) }.

#show sudoku/3.