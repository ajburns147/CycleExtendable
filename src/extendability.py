import time


def cycleIsExtendable(adjMatrix):
    start_time = time.time()

    num_vertices = len(adjMatrix)

    cycles = set()
    print(time.time() - start_time)


    # cycles2 = allCycles2(adjMatrix)

    allPathsWrapper(num_vertices, cycles, adjMatrix)
    print(time.time() - start_time)

    print(f"{cycles=}")
    # print(f"{cycles2=}")

    num_vertices = len(adjMatrix)

    response = cycleLoop(cycles, num_vertices)
    print(time.time() - start_time)

    return response


def myDFS(graph, start, end):
    stack = [(start, [])]
    while stack:
        curr, path = stack.pop()
        if path and curr == end:
            yield path
            continue
        for i in range(0, len(graph)):
            # print(f"{i=} {curr=}")
            # if curr > len(graph) - 1:
            #     continue
            if graph[i][curr] == 0:
                continue
            next_vertex = i
            if next_vertex in path:
                continue
            stack.append((next_vertex, path + [next_vertex]))


def allCycles(adjMatrix):

    cycles = [[node]+path for node in range(0, len(adjMatrix)) for path in myDFS(adjMatrix, node, node)]
    print(f"{cycles=}")
    # cycles = set(map(frozenset, cycles)
    cycle_set = set()
    for i in cycles:
        cycle_set.add(frozenset(i))
    # cycles = set(cycles)
    return cycle_set
    # print(cycles)

def allCycles2(adjMatrix):
    cycles = [[node]+path for node in range(0, len(adjMatrix)) for path in myDFS(adjMatrix, node, node)]

    # print(cycles)
    cycles = set(map(frozenset, cycles))

    cycles_final = cycles.copy()

    set_copy = True

    while set_copy:
        set_copy = False
        cycles_group = set()

        for i in cycles:
            for j in cycles:
                intersect = i.intersection(j)
                if len(intersect) > 0 and len(intersect) != len(i):
                    cycles_group.add(i.union(j))
                    cycles_final.add(i.union(j))
                    set_copy = True
        cycles = cycles_group.copy()


    return cycles_final


def allPathsWrapper(num_vertices, cycles, adjMatrix):
    path = []
    visited = set()
    allPaths(0, num_vertices - 1, visited, path, cycles, adjMatrix)


def allPaths(u, d, visited, path, cycles, adjMatrix):
    # Mark the current node as visited and store in path

    visited.add(u)
    path.append(u)

    # If current vertex is same as destination, then print
    # current path[]

    if u == d:
        # print(path)
        cycles.add(frozenset(path))
        # print(f"{cycles=}")
    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex

        for i in enumerate(adjMatrix[u]):
            if i[1] == "0":
                continue

            if i[0] not in visited:
                allPaths(i[0], d, visited, path, cycles, adjMatrix)

    # Remove current vertex from path[] and mark it as unvisited
    path.pop()
    visited.remove(u)


def cycleLoop(cycles, num_vertices):
    # print(f"{cycles=}")
    for i in cycles:
        cycle_extendable = False

        if len(i) == num_vertices:
            continue

        for j in cycles:
            if len(j) != len(i) + 1:
                continue

            if i.issubset(j):
                # print(True)
                cycle_extendable = True
                break
        if not cycle_extendable:
            return False
    return True


default_adjMatrix = [
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0],
]

counter_example = [
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

# print(cycleIsExtendable(default_adjMatrix))
print(cycleIsExtendable(counter_example))
