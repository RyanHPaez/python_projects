def solution(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    output = []
    for row in range(len(matrix)):
        r = []
        output.append(r)
        for column in range(len(matrix[0])):
            output[row].append(int("0"))           
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == True:
                if column + 1 < num_columns:
                    output[row][column+1] += 1
                if column > 0: 
                    output[row][column-1] += 1
                if row + 1 < num_rows:
                    output[row+1][column] += 1
                if row > 0: 
                    output[row-1][column] += 1
                if column > 0 and row > 0:
                    output[row-1][column-1] += 1
                if column + 1 < num_columns and row + 1 < num_rows:
                    output[row+1][column+1] += 1
                if row + 1 < num_rows and column > 0:
                    output[row+1][column-1] += 1
                if row > 0 and column + 1 < num_columns:
                    output[row-1][column+1] += 1
    return output 