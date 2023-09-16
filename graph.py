from __future__ import annotations
from typing import Iterator


class Graph:
    __matrix: list[list[int]]
    __vertexes: list[str]

    def __init__(self):
        self.__matrix = []
        self.__vertexes = []

    def __check_vertex_is_exist(self, name: str):
        if name not in self.__vertexes:
            raise Exception(f'Vertex {name} is not exist.')

    def __get_index_vertex_with_name(self, name: str) -> int:
        self.__check_vertex_is_exist(name)

        return self.__vertexes.index(name)

    def first(self) -> str:
        if not len(self.__vertexes):
            raise Exception('Graph is empty')

        return self.__vertexes[0]

    def get_count_rows(self) -> int:
        return len(self.__matrix)

    def add_v(self, name: str):
        for row in self.__matrix:
            row.append(0)

        new_size = self.get_count_rows() + 1
        self.__matrix.append([0] * new_size)

        self.__vertexes.append(name)

    def add_e(self, source: str, target: str):
        source_index = self.__get_index_vertex_with_name(source)
        target_index = self.__get_index_vertex_with_name(target)

        self.__matrix[source_index][target_index] = 1

    def get_available_vertex(self, source: str) -> Iterator[str]:
        source_index = self.__get_index_vertex_with_name(source)

        for index, col in enumerate(self.__matrix[source_index]):
            if col:
                yield self.__vertexes[index]

    def get_transpose_graph(self) -> Graph:
        g_trans = Graph()

        for vertex in self.__vertexes:
            g_trans.add_v(vertex)

        for from_vertex in self.__vertexes:
            for to_vertex in self.get_available_vertex(from_vertex):
                g_trans.add_e(source=to_vertex, target=from_vertex)

        return g_trans
