matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


def row_sums(m):
    return [sum(row) for row in m]


def column_sums(m):
    return [sum(row[j] for row in m) for j in range(len(m[0]))]


def diagonal(m):
    return [m[i][i] for i in range(min(len(m), len(m[0])))]


def transpose(m):
    return [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]


def flatten(m):
    return [value for row in m for value in row]


def multiply(a, b):
    if len(a[0]) != len(b):
        raise ValueError(
            f"Cannot multiply: {len(a)}x{len(a[0])} by {len(b)}x{len(b[0])} "
            f"(columns of A must equal rows of B)"
        )
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def run_all(m, label):
    print(f"--- {label} ---")
    print("row_sums:   ", row_sums(m))
    print("column_sums:", column_sums(m))
    print("diagonal:   ", diagonal(m))
    print("transpose:  ", transpose(m))
    print("flatten:    ", flatten(m))


if __name__ == "__main__":
    run_all(matrix, "square 3x3")

    rect = [[1, 2, 3], [4, 5, 6]]
    run_all(rect, "rectangular 2x3")

    print("--- stretch: multiply ---")
    print(multiply(rect, transpose(rect)))
    try:
        multiply(rect, rect)
    except ValueError as e:
        print("Error:", e)