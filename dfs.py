from graph import Graph


def dfs(v: str, order: list[str], used: dict[str, bool], g: Graph):
    used[v] = True

    for vertex in g.get_available_vertex(v):
        if not used[vertex]:
            dfs(vertex, order, used, g)

    order.append(v)


def dfs_transpose(v: str, component: list[str], used: dict[str, bool], g_t: Graph):
    used[v] = True
    component.append(v)

    for vertex in g_t.get_available_vertex(v):
        if not used[vertex]:
            dfs_transpose(vertex, component, used, g_t)
