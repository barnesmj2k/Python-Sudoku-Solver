import random
import sys
import copy

d = 0
n, m = (9,9)
puzzle = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
error = False
    

def printPuzzle(g):
    if (not isSolved(g)):
        print(r""" ____            _       _          
/ ___| _   _  __| | ___ | | ___   _ 
\___ \| | | |/ _` |/ _ \| |/ / | | |
 ___) | |_| | (_| | (_) |   <| |_| |
|____/ \__,_|\__,_|\___/|_|\_\\__,_|""")

    else:
        print(r""" ____        _                
/ ___|  ___ | |_   _____ _ __ 
\___ \ / _ \| \ \ / / _ \ '__|
 ___) | (_) | |\ V /  __/ |   
|____/ \___/|_| \_/ \___|_|   """)

    print(" -------------------")
    s = ""
    for i in range(n):
        if (i % 3 == 0 and i != 0):
            s += (" -------------------\n")

        #start j loop
        for j in range(m):

            if (j % 3 == 0):
                s += " | "

            s += str(g[i][j])
            #end j loop    
        s+= " |\n"

    s += (" -------------------")    
    print(s)
    
def solvePuzzle(p, d):
    if (d > 24):
        print("Program ran " +str(d) + " times.\nNot possible with basic solve.\nTrying complex solve...")
        return complexSolve(p)
    for i in range(n):
        for j in range(m):
            var = p[i][j]
            if (var == 0):
                domain = [1,2,3,4,5,6,7,8,9]
                checker(p, i, j, domain)
                if (len(domain) == 1):
                     p[i][j] = domain[0]
    if (isSolved(p)):
        return p
    else:
        return solvePuzzle(p, d+1)

def checker(p, i, j, domain):
    row = 0
    col = 0
    for row in range(n):
            if (p[row][j] in domain):
                domain.remove(p[row][j])
    for col in range(m):
            if (p[i][col] in domain):
                domain.remove(p[i][col])

    gridRow = (i // 3) * 3
    gridCol = (j // 3) * 3

    for row in range(gridRow, gridRow + 3):
        for col in range(gridCol, gridCol + 3):
            if p[row][col] in domain:
                domain.remove(p[row][col])

def isSolved(p):
    return all(0 not in row for row in p)

def complexSolve(p):
    for i in range(n):
        for j in range(m):
            var = p[i][j]
            if (var == 0):
                domain = [1,2,3,4,5,6,7,8,9]
                checker(p, i, j, domain)

                if not domain:
                    return None #backtrackk
                
                for value in domain:
                    tempGrid = copy.deepcopy(p)
                    tempGrid[i][j] = value
                    result = complexSolve(tempGrid)
                    if result:
                        return result #successful
                
                return None #no valid solution

    if (isSolved(p)):
        return p
    else:
        return None

# grid = makeGrid(emptyGrid)
printPuzzle(puzzle)
solution = solvePuzzle(puzzle, d)
printPuzzle(solution)