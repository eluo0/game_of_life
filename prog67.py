## prog67.py
## Elle Luo
## August 2, 2017
##
## ECS 10 - Summer 2017
## Programming Assignment 6 & 7


## Programming Assignment 6

glider =[[0,0,0,0,0,0,0],
 [0,0,1,0,0,0,0],
 [0,0,0,1,0,0,0],
 [0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0]]

def checkCell(grid_table, row, column): ## check neighbor cells & count how many 1s
    """ expect argument grid, the table. Function purpose: check neighbor cells and count
        how many 1s are there in the neighbor cells, row 0 is in the same row
        of the centre cell, row -1 is the row above the centre cell, row 1 is
        the row below the centre cell.
        Expect other arguments row and column.                                          """


    new_row = row
    new_column = column
    countFromLeft = -1  # left column -1, center 0, right 1
    numberOfOne = 0
    OneOrZero1 = 0  ## number of ones at the top row
    OneOrZero2 = 0  ## number of ones at the bottom row
    OneOrZero3 = 0  ## number of ones in the middle row, exclude the cell in the center
    
    while countFromLeft < 2:
        if new_column == 6:
            oneOrZero4 = grid_table[new_row-1][new_column]
            oneOrZero5 = grid_table[new_row][new_column]
            oneOrZero6 = grid_table[new_row + 1][new_column]

        if new_column + countFromLeft == 6: 
            
            oneOrZero1 = 0
        else:
            oneOrZero1 = grid_table[new_row - 1][new_column + countFromLeft] ## the numbers in row -1, the top row
        
            
        if new_row + 1 >= 6:  ## when new_row == 6, the cell doesn' have bottom row to count ones
            oneOrZero2 = 0
            
        else:
            oneOrZero2 = grid_table[new_row + 1][new_column + countFromLeft]  ## row 1, the bottom row
                
        
        
        if grid_table[new_row][new_column] == 0 or grid_table[new_row][new_column] == 1: ## the spot of center cell which doesn't count
        
           
            if countFromLeft == 0:
                oneOrZero3 = 0
            else:
                oneOrZero3 = grid_table[new_row][new_column + countFromLeft] ## row 0, row in the middle
                
            
        
        if oneOrZero1 == 1:
            numberOfOne = numberOfOne + oneOrZero1
        else:
            numberOfOne = numberOfOne + 0
            
        if oneOrZero2 == 1:
            numberOfOne = numberOfOne + oneOrZero2
        else:
            numberOfOne = numberOfOne + 0
            
        if oneOrZero3 == 1:
            numberOfOne = numberOfOne + oneOrZero3
            
        else:
            numberOfOne = numberOfOne + 0
                
        countFromLeft = countFromLeft + 1
        
    return numberOfOne





def convert(grid_table):
    """ fuction 'convert' expect argument grid_table, this function does the convert work
        to convert the number of neighbor cells that contained in each cell into a grid format,
        meaning the each value in a single grid represents the number of neighbor cells in this grid. """
    
    list_grid2 = []
    new_grid2 = []
    column = 0
    row = 0
    while column <= 7 and row <= 6:  ## counting ones at the bottom rows for each cell
        neighborCell = checkCell(grid_table, row, column)
        column = column + 1
        
        list_grid2.append(neighborCell)
        if column == 6:
            
            row = row + 1
            column = 0
            new_grid2 = new_grid2 + [list_grid2 + [0]]
            list_grid2 = []
            if row==6:
               ## print("this is convert", new_grid2)
                return new_grid2
            



def original(grid_table):
    """ function 'original' does the work to convert all the 0s and 1s into
        a grid format.                                                       """
    
    cell = 0  ## initialize cell
    column = 0
    row = 0
    list_grid = []
    new_grid = []
    
    
        
    while column <=7 and row <= 6:
        eachCell = grid_table[row][column]
        
        
        list_grid.append(eachCell)
        column = column + 1
        if column == 7:
           column = 0
           row = row + 1
           new_grid = new_grid + [list_grid]
           list_grid = []
           if row == 6:
               return new_grid
        
def nextGen(grid_table):
    """ function 'nextGen' does the work to convert original grid and generate the
        next generation of cells.                                                 """
    
    convertV = convert(grid_table)
    originalV = original(grid_table)
    col = 0
    row = 0
    list_grid = []
    table = []
    cell = 0
    while col <= 7 and row <= 5: ## 6
        neighborCell = convertV[row][col]
        originalCell = originalV[row][col]
        
        if originalCell == 1 and neighborCell < 2: ## live cell die when neighbor cell < 2
            cell = 0
        elif originalCell == 1 and neighborCell == 2: ## live cell lives on the next generation
            cell = 1
        elif originalCell == 1 and neighborCell == 3:
            cell = 1
        elif originalCell == 0 and neighborCell == 3: ## dead cell become alive when neighbor cell == 3
            cell = 1
        elif originalCell == 1 and neighborCell > 3: ## live cell die when neighbor cell > 3
            cell = 0
        else:
            cell = 0

        list_grid.append(cell)
            
        col = col + 1
       
        if col == 7:
            row = row + 1
            col = 0
            table = table + [list_grid]
            list_grid = []
            if row == 6:
                return table



## Programming assignment 7


def convertToSpecialCharacter(grid_table):
    """ function 'convertToSpecialCharacter' does the work to convert all the 0s and 1s
        into the characters of . and *                                                  """
    
    list_grid = ''
    table = ''
    grid_table2 = ''
    i = 0  ## row
    j = 0  ## column
    cell = 0
    for row in grid_table:
        for col in row:
            if i <= 6 and j <=7:
                if col == 0:
                    cell = '.' 
                    j = j + 1
                    list_grid = list_grid + cell
                    
                elif col == 1:
                    cell = '*' 
                    j = j + 1
                    list_grid = list_grid + cell
                else:
                    pass
                
                
                if j == 7:
                    i = i + 1
                    j = 0
                    list_grid = list_grid + "\n"
                    if i == 6:
                        return(list_grid)
            
                



def life():
    """ function 'life' is the main function of this program that imports the text file,
        generates each generations of cells, and save the last generation into a text file. """
    
    list_grid = []
    table = []
    row = 0
    col = 0
    grid_table2 = []
    while True:
        filename = input("Enter input file name: ")
        try:
            inFile = open(filename, "r")
            break
        except:
            print("No such file, Try again.")
            
    list_grid = []

    for line in inFile:    ## read file
        for character in line:
            if col <= 7 and row <= 6:
                if character == "\n":
                    pass
                else:
                    character = int(character)
                    list_grid.append(character)
                    col = col + 1
                if col == 7:
                    row = row + 1
                    col = 0
                    table.append(list_grid)
                    list_grid = []
                    if row == 6:
                        grid_table2 = grid_table2 + table
                       ## print("grid_table2", grid_table2)
                        
                
    inFile.close()

    while True:
        number_generation = input("How many new generations would you like to print? ")
        try:
            number_generation = int(number_generation)
            break
        except:
            print("Not a valid number.")

    

    table = 0
    iterations = 0
    

    generationNumbers = 0
    while generationNumbers <= number_generation:
        print("Generation: ", generationNumbers, "\n",  convertToSpecialCharacter(grid_table2))
        if generationNumbers == number_generation:
            finalV= grid_table2
        grid_table2 = nextGen(grid_table2)
        generationNumbers = generationNumbers + 1
        
    i = 0  ## row
    j = 0  ## col
    emptystr = ""
    for row in finalV:
        for col in row:
            if j <= 7 and i <= 6:
                col = str(col)
                emptystr = emptystr + col
                j = j + 1
                if j == 7:
                    emptystr = emptystr + "\n"
                    i = i + 1
                    j = 0
                    
                
        
    saveOrNot = input("Would you like to save the latest generation? ('y' to save): ")
    if saveOrNot == 'y':
        newFileName = input("Enter destination file name: ")
        overwrite = input("Do you want to overwrite that file? ('y' to continue): ")
        if overwrite == 'y':
            someFile = open(newFileName, 'w')
            for row in emptystr:
                someFile.write(row)
                    
        else:
            newFileName = input("Enter destination file name: ")
            someFile = open(newFileName, 'w')
            for row in emptystr:
                someFile.write(row)
            print("Saving data to", newFileName)
            someFile.close()
            print("End of Program.")
            return
                    
            

        print("Saving data to", newFileName)
        someFile.close()

        print("End of program.")
        return
         
    elif saveOrNot == 'n':
        print("End of program.")
        return

    else:
        pass
    
    print("End of program.")
    return
                
                




