"""rush/ex00/main.py"""
from check import check

def main():
    """have board and call check"""
    board = """\
P...
....
....
..K.\
"""
    board2 = """\
B....
.P...
..B..
....P
R...K\
"""
    board3 = """\
BK.PR
..P..
..Q..
.....
R....\
"""
    board4 = """\
B...B
.P...
..Q..
...P.
R.P.K\
"""
    boardt = """\
.B..
..K.
....
....\
"""
    check(boardt)

main()