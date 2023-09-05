# https://edabit.com/challenge/3DAkZHv2LZjgqWbvW

def adjacent(
    adjacency_matrix: list[list[int]],
    node_pair: tuple[int]
) -> bool:
    return adjacency_matrix[node_pair[0]][node_pair[1]]

def test():
    matrix_1 = [
        [ 0, 1, 0, 0 ],
        [ 1, 0, 1, 1 ],
        [ 0, 1, 0, 1 ],
        [ 0, 1, 1, 0 ]
    ]
    assert adjacent(matrix_1, (0, 1))
    assert not adjacent(matrix_1, (0, 2))

    matrix_2 = [
        [ 0, 1, 0, 1, 1 ],
        [ 1, 0, 1, 0, 0 ],
        [ 0, 1, 0, 1, 0 ],
        [ 1, 0, 1, 0, 1 ],
        [ 1, 0, 0, 1, 0 ]
    ]
    assert adjacent(matrix_2, (0, 3))
    assert not adjacent(matrix_2, (1, 4))

if __name__ == "__main__":
    test()