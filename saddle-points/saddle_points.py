def saddle_points(matrix):

    
    saddle = list()
    if len(matrix) == 0:
        return saddle
    lenRow = len(matrix[0])
    for row in matrix:
        if len(row) != lenRow:
            raise ValueError("Not gut!")
        else:
            lenRow = len(row)
        
    saddle = list()
    
    index2 = 1
    for row in matrix:
        rowCpy = row.copy()
        maxRowValIndx = list()
        maxRowValIndx.append(rowCpy.index(max(rowCpy)))
        rowCpy.remove(max(rowCpy))
        index = 1
        while rowCpy and max(rowCpy) == max(row):
            maxRowValIndx.append(rowCpy.index(max(rowCpy))+index)
            rowCpy.remove(max(rowCpy))
            index += 1
        
        for rowIndx in maxRowValIndx:
            column = [matrix[val][rowIndx] for val in range(len(matrix))]
            if min(column) == row[rowIndx]:
                saddle.append({"row": index2, "column": rowIndx+1})

        index2 += 1

    return saddle    
            
