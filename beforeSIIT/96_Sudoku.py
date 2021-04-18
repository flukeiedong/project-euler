
def table(sudoku):
    table = []
    divide = [3, 6 ,9]
    for x in divide:
        for y in divide:
            sub_table = []
            for t in range(y-3, y):
                sub_table += sudoku[t][:x]
            table.append(sub_table)
    return table

demo = """003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300"""

horizontal = [list(i) for i in demo.split("\n")]
print(horizontal)




#for i in range(50):
