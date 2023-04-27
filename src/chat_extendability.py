import networkx as nx
from graph6_conversion import graph6ToAdj


def is_cycle_extendable(graph6):
    """
    Determines if a given graph G is cycle extendable.
    """
    # Convert the graph6 string to a NetworkX graph object
    G = nx.from_graph6_bytes(graph6.encode('ascii'))

    # Iterate through each cycle in the graph's cycle basis
    for C in nx.cycle_basis(G):

        # Check if C is a chordless cycle
        if len(C) == len(set(C)):

            # Create a set of vertices that includes C and its neighbors
            C_plus = set(C)
            for v in C:
                C_plus.update(set(nx.neighbors(G, v)))

            # Iterate through each vertex u in C's neighbors
            for u in C:

                # Iterate through each vertex v that is not in C_plus
                for v in set(nx.neighbors(G, u)).difference(C_plus):

                    # Create a new cycle C_prime by adding v to C
                    C_prime = C + [v]

                    # Check if C_prime is a cycle and if it extends C
                    if nx.cycle_basis(nx.subgraph(G, C_prime))[0] != C_prime:
                        return False

    # If no C_prime failed the check, return True
    return True


def is_connected(graph6: str) -> bool:
    G = nx.from_graph6_bytes(graph6.encode('ascii'))
    if nx.is_connected(G):
        return True
    return False


def is_chordal(graph6: str) -> bool:
    G = nx.from_graph6_bytes(graph6.encode('ascii'))
    if nx.is_chordal(G):
        return True
    return False


def is_hamiltonian(graph6):
    adj_matrix = graph6ToAdj(graph6)

    # Determine the number of vertices in the graph
    num_vertices = len(adj_matrix)

    # Create a list to keep track of the visited vertices
    visited = [False] * num_vertices

    # Create a stack to keep track of the path
    stack = []

    # Define a recursive function to search for a Hamiltonian cycle
    def search(vertex, depth):
        # Mark the current vertex as visited
        visited[vertex] = True

        # Add the current vertex to the path
        stack.append(vertex)

        # If the path contains all the vertices, it is a Hamiltonian cycle
        if depth == num_vertices:
            if adj_matrix[stack[-1]][stack[0]] == 1:
                return True
        else:
            # Check all the neighbors of the current vertex
            for neighbor in range(num_vertices):
                if adj_matrix[vertex][neighbor] == 1 and not visited[neighbor]:
                    # If a Hamiltonian cycle is found, return True
                    if search(neighbor, depth + 1):
                        return True

        # Remove the current vertex from the path and mark it as unvisited
        visited[vertex] = False
        stack.pop()

        # If no Hamiltonian cycle is found, return False
        return False

    # Search for a Hamiltonian cycle starting from each vertex
    for start_vertex in range(num_vertices):
        if search(start_vertex, 1):
            return True

    # If no Hamiltonian cycle is found, return False
    return False


if __name__ == "__main__":
    graphs = [
        "E???",
        "EEjw",
        "ECO_",
        "N|cdwEB_gCo@c___oAG",
        "EEjw",
        "EElw",
        "EEnw",
        "EE~w",
    ]

    for i in graphs:
        if is_hamiltonian(i):
            print(f"{is_cycle_extendable(i)=}")
            # print(is_hamiltonian(i))
            print(f"{is_connected(i)=}")
            print()