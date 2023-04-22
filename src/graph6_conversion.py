def adjToGraph6(adjMatrix):
    elements_from_row = 0
    bin_list = ""

    # Take lower left diagonal matrix and append rows to string
    for row in adjMatrix:
        elements_from_row += 1
        if elements_from_row == 1:  # Ignore first row
            continue
        row_elements = list(map(str, row[0:elements_from_row - 1]))
        bin_list += "".join(row_elements)

    # Pad on right with 0s until len is a multiple of 6
    if len(bin_list) % 6 != 0:
        bin_list += "0" * (6 - len(bin_list) % 6)

    # Split into 6 bit pieces
    chunks = [bin_list[i:i + 6] for i in range(0, len(bin_list), 6)]

    # vertices + 63 = first char
    graph6 = chr(len(adjMatrix) + 63)

    # Take chr of the int each piece and add to graph6
    for i in chunks:
        graph6 += chr(int(i, 2) + 63)

    return graph6


def graph6ToAdj(graph6):
    # vertices + 63 = first char
    vertices = ord(graph6[0]) - 63

    bin_list = ""

    # Turn into 6 bit pieces
    for i in graph6[1:]:
        bin_list += ("{0:06b}".format(ord(i) - 63))

    adjMatrix = []

    # Unpad on right until have bottom left diag
    num_in_bot_left_diag = 0
    for i in range(vertices):
        num_in_bot_left_diag += i

    bot_left_diag = bin_list[:num_in_bot_left_diag]

    for i in range(0, vertices):
        sub_adjMatrix = [0 for i in range(vertices)]
        for j in range(i):
            sub_adjMatrix[j] = int(bin_list[0])
            bin_list = bin_list[1:]
        adjMatrix.append(sub_adjMatrix)

    addTranspose(adjMatrix)

    return adjMatrix


def addTranspose(adjMatrix):
    for j in range(len(adjMatrix)):
        for i in range(j):
            adjMatrix[i][j] = adjMatrix[j][i]


if __name__ == "__main__":
    print(adjToGraph6([
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0],
    ]))

    for i in (graph6ToAdj("DQc")):
        print(i)

    # counter_example = [
    #     [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    #     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    #     [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    #     [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    #     [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
    #     [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    #     [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    #     [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
    #     [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    #     [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #     [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    # ]

    counter_example = [

        [0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    ]

    print(adjToGraph6(counter_example))  # N|cdwEB_gCo@c___oAG
    # print(adjToGraph6(counter_example))  # N|eGLk@gKA_@nV??O_G

    # for i in (graph6ToAdj("E?A?")):
    #     print(i)
