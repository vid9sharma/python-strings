# Prints a list of lists in a well-formatted table with each column right-justified.

tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

def printTable(table):
    columnWidths = [0] * len(table)
    
    # Calculate the maximum width of each column
    for i in range(len(table)):
        for item in table[i]:
            columnWidths[i] = max(columnWidths[i], len(item))
        
    # Print each row with the appropriate padding
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(columnWidths[j]), end=' ')
        print()

printTable(tableData)
