from multiprocessing import Pool


A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

B = [
    [1, 0, 2, 1],
    [0, 1, 0, 2],
    [2, 0, 1, 0],
    [1, 2, 0, 1]
]

# Function to compute one row of result
def multiply_row(row):
    result_row = []
    for j in range(len(B[0])):   # For each column in B
        sum_value = 0
        for k in range(len(B)):  # For each element in row
            sum_value += row[k] * B[k][j]
        result_row.append(sum_value)
    return result_row

if __name__ == "__main__":
    with Pool() as p:
        result = p.map(multiply_row, A)

    print("Result Matrix:")
    for row in result:
        print(row)