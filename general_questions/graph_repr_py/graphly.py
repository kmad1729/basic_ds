'representation and analysis of graphs in python'
import unittest

#this graph is python representation of graphly_pic.jpg
graph = {
            'A': ['B', 'C'],
            'B': ['C', 'D'],
            'C': ['D'],
            'E': ['F'],
            'F': ['C'],
        }

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path

    if not graph.has_key(start):
        return None

    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


class Test_find_path(unittest.TestCase):

    def test_positive_tc(self):
        exp_paths = [
                ['A', 'B', 'D', 'C'],
                ['E', 'F', 'C', 'D'],
                ['A', 'B', 'D'],
                ['A', 'B', 'C', 'D'],
                ]

        self.assertTrue(find_path(graph, 'A', 'D') in exp_paths)
        self.assertTrue(find_path(graph, 'E', 'D') in exp_paths)
        self.assertTrue(find_path(graph, 'E', 'E'), ['E'])
        self.assertTrue(find_path(graph, 'E', 'D') is not None)

    def test_negative_tc(self):
        self.assertTrue(find_path(graph, 'A', 'E') is None)
        self.assertTrue(find_path(graph, 'E', 'A') is None)
        self.assertTrue(find_path(graph, 'E', 'B') is None)

if __name__ == '__main__':
    unittest.main()
