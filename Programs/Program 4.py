import random
def transpose(M):
    matrix = []
    for x in range(len(M)):
        matrix.append([])
        for y in range(len(M[0])):
            matrix[x].append(M[y][x])
    return matrix
    
if __name__ == '__main__':
    dimensions = random.randint(3,5)
    matrix = [ [ random.randint(10,99) for i in range(dimensions) ] \
               for i in range(dimensions) ]
    print('Original matrix M:\n' + '\n'.join([str(row) for row in matrix]) )
    print('\nTransposed matrix:\n' + '\n'.join([str(row) for row in transpose(matrix)]) )
    print('\nRe-printing original matrix M to make sure you did not change it:')
    print('\n'.join([str(row) for row in matrix]) )