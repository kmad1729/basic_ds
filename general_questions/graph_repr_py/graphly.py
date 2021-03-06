'representation and analysis of graphs in python'
import unittest

#this graph is python representation of graphly_pic.jpg
graph = {
            'A': ['B', 'C'],
            'B': ['C', 'D'],
            'C': ['D'],
            'D': ['C'],
            'E': ['F', 'G'],
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


def find_all_paths(graph, start, end, path = []):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []

    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths
            
def find_shortest_path(graph, start, end, path = []):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest_path = None
    for node in graph[start]:
        if node not in path:
            new_path = find_shortest_path(graph, node, end, path)
            if new_path:
                if not shortest_path or len(new_path) < len(shortest_path):
                    shortest_path = new_path
    return shortest_path



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
        self.assertTrue(find_path(graph, 'G', 'E') is None)

class Test_find_all_paths(unittest.TestCase):

    def test_positive_tc(self):
        A_D_paths = [
                ['A', 'B', 'D'],
                ['A', 'B', 'C', 'D'],
                ['A', 'C', 'D'],
            ]
        computed_A_D_paths = find_all_paths(graph, 'A', 'D')
        for pth in A_D_paths:
            self.assertTrue(pth in computed_A_D_paths)

    def test_neg_tc(self):
        self.assertTrue(find_all_paths(graph, 'A', 'G') == [])
        self.assertTrue(find_all_paths(graph, 'G', 'A') == [])
        self.assertTrue(find_all_paths(graph, 'F', 'E') == [])

class Test_find_shortest_path(unittest.TestCase):

    def test_positive_tc(self):
        self.assertEquals(find_shortest_path(graph, 'A', 'D'), ['A', 'B', 'D'])
        self.assertEquals(find_shortest_path(graph, 'A', 'C'), ['A', 'C'])
        self.assertEquals(find_shortest_path(graph, 'E', 'F'), ['E', 'F'])
        self.assertEquals(find_shortest_path(graph, 'A', 'B'), ['A', 'B'])
        self.assertEquals(find_shortest_path(graph, 'B', 'D'), ['B', 'D'])
        self.assertEquals(find_shortest_path(graph, 'D', 'C'), ['D', 'C'])
        self.assertEquals(find_shortest_path(graph, 'C', 'D'), ['C', 'D'])

    def test_negative_tc(self):
        self.assertTrue(find_shortest_path(graph, 'B', 'F') == None)
        self.assertTrue(find_shortest_path(graph, 'E', 'A') == None)
        self.assertTrue(find_shortest_path(graph, 'G', 'A') == None)
if __name__ == '__main__':
    unittest.main()
