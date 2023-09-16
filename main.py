from graph import Graph
from dfs import dfs, dfs_transpose


VERTEXES_NAMES: list[str] = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
]

EDGES: list[dict[str, str]] = [
    {"source": "A", "target": "B"},  # A -> B
    {"source": "B", "target": "E"},  # B -> E
    {"source": "B", "target": "F"},  # B -> F
    {"source": "B", "target": "C"},  # B -> C
    {"source": "C", "target": "G"},  # C -> G
    {"source": "C", "target": "D"},  # C -> D
    {"source": "D", "target": "C"},  # D -> C
    {"source": "D", "target": "H"},  # D -> H
    {"source": "E", "target": "A"},  # E -> A
    {"source": "E", "target": "F"},  # E -> F
    {"source": "F", "target": "G"},  # F -> G
    {"source": "G", "target": "F"},  # G -> F
    {"source": "H", "target": "G"},  # H -> G
    {"source": "H", "target": "D"},  # H -> D
]


def __init_graph() -> Graph:
    g = Graph()

    for vertex in VERTEXES_NAMES:
        g.add_v(vertex)

    for edges in EDGES:
        g.add_e(**edges)

    return g


def __init_used() -> dict[str, bool]:
    result = {}
    for vertex in VERTEXES_NAMES:
        result[vertex] = False

    return result


if __name__ == '__main__':
    graph = __init_graph()
    graph_trans = graph.get_transpose_graph()

    used = __init_used()
    order: list[str] = []

    for vertex in graph.get_available_vertex(graph.first()):
        dfs(vertex, order, used, graph)

    used = __init_used()
    component: list[str] = []

    order.reverse()
    for vertex in order:
        if not used[vertex]:
            dfs_transpose(vertex, component, used, graph_trans)

            print(", ".join(component))

            component.clear()
