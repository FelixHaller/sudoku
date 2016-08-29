Sudoku
++++++

Just a collection of algorithmns related to the *sudoku* game.

usage
=====

solve
-----

To solve a sudoku you have to write it into a text file. Empty fields can
be represented by any non-digit character. You can also write all numbers in a single
line.

Example:

.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/240px-Sudoku-by-L2G-20050714.svg.png

File Example 1:

::

    53__7____
    6__195___
    _98____6_
    8___6___3
    4__8_3__1
    7___2___6
    _6____28_
    ___419__5
    ____8__79

File Example 2:

::

    53__7____6__195____98____6_8___6___34__8_3__17___2___6_6____28____419__5____8__79

then run:

::

    $ python3 main.py <filename>


development
===========


supported features
------------------

* solve simple Sudokus

planned features
----------------

* solve more sudokus
