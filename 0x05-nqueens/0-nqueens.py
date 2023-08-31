#!/usr/bin/python3
"""
Solution 
"""
import sys


def backtrack(cr, cn, ccols, cpos, cneg, cboard):
    """
    backtrack 
    """
    if cr == cn:
        res = []
        for l in range(len(cboard)):
            for k in range(len(cboard[l])):
                if cboard[l][k] == 1:
                    res.append([l, k])
        print(res)
        return

    for c in range(cn):
        if c in ccols or (cr + c) in cpos or (cr - c) in cneg:
            continue

        ccols.add(c)
        cpos.add(cr + c)
        cneg.add(cr - c)
        cboard[cr][c] = 1

        backtrack(cr+1, n, ccols, cpos, cneg, cboard)

        ccols.remove(c)
        cpos.remove(cr + c)
        cneg.remove(cr - c)
        cboard[cr][c] = 0


def nqueens(n):
    """
    Solut
    """
    ccols = set()
    cpos_diag = set()
    cneg_diag = set()
    cboard = [[0] * n for i in range(n)]

    backtrack(0, n, ccols, cpos_diag, cneg_diag, cboard)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
