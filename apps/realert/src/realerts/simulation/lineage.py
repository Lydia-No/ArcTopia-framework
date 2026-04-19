import networkx as nx


class LineageGraph:

    def __init__(self):

        self.graph = nx.DiGraph()

    def add_resource(self, resource_id):

        self.graph.add_node(resource_id)

    def add_transformation(self, parent, child):

        self.graph.add_edge(parent, child)

    def children(self, resource_id):

        return list(self.graph.successors(resource_id))
