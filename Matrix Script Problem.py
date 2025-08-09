import re

def decode_matrix_script():
    # Read the first line to get N and M
    N, M = map(int, input().split())
    
    # Read the next N lines as the matrix rows
    matrix = [input().strip() for _ in range(N)]
    
    # Transpose the matrix to read columns as rows
    transposed = list(zip(*matrix))
    
    # Concatenate each column's characters to form the initial decoded string
    decoded = ''.join([''.join(column) for column in transposed])
    
    # Use regex to replace non-alphanumeric sequences between alphanumeric characters with a space
    # The pattern matches one or more non-alphanumeric characters between two alphanumeric characters
    pattern = r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])'
    processed = re.sub(pattern, ' ', decoded)
    
    print(processed)

decode_matrix_script()