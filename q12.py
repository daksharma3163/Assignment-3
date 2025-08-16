def flatten_matrix(matrix):
    flattened = []
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            flattened.append(matrix[i][j])
    
    return flattened

input_str = input("Enter matrix rows separated by commas: ")
rows = input_str.strip().split(',')
matrix = [list(map(int, row.strip().split())) for row in rows]

flattened = flatten_matrix(matrix)
for element in flattened:
    print(element,end=', ')
