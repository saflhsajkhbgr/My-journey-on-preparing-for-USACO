import re
import matplotlib.pyplot as plt
class Vertex:
    # 邻接列表构图，每个node保存与本节点相连的节点
    def __init__(self, key):
        # 顶点的key
        self.id = key
        # 用于保存和哪些点相连，key为node的key，val为连接权重
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        # 添加与某个node的连接，连接key为该节点key，值为权重
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    # 获取与本节点相连的所有节点key
    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        # 顶点集合
        self.vertList = {}
        # 顶点的数量
        self.numVertices = 0

    def addVertex(self, key):
        # 添加顶点数量
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        # 这的key就是代表这个顶点的变量
        self.vertList[key] = newVertex
        # 此处为什么要将这个顶点返回呢
        return newVertex

    def getVertex(self, n):
        # 遍历图中所有的顶点
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        # 判断图中是否存在这个顶点
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        # 给两个顶点添加边
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    # 获取所有的边
    def getVertices(self):
        return self.vertList.keys()

    # 遍历这个图结构
    def __iter__(self):
        return iter(self.vertList.values())

g = Graph()
for i in range(6):
    g.addVertex(i)

print(g.vertList)

g.addEdge(0, 1, 5)
g.addEdge(0, 5, 2)
g.addEdge(1, 2, 4)
g.addEdge(2, 3, 9)
g.addEdge(3, 4, 7)
g.addEdge(3, 5, 3)
g.addEdge(4, 0, 1)
g.addEdge(5, 4, 8)
g.addEdge(5, 2, 1)
for v in g:
    for w in v.getConnections():
        temp=w.getId()
        number=g.vertList[w.getId()]
        print("( %s , %s , %s )" % (v.getId(), w.getId(), v.connectedTo[number]))


def create_directed_graph_from_edges(my_graph):#用边生成有向图
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    edge_list = [('A', 'F', 9), ('A', 'B', 10), ('A', 'G', 15), ('B', 'F', 2),
                 ('G', 'F', 3), ('G', 'E', 12), ('G', 'C', 10), ('C', 'E', 1),
                 ('E', 'D', 7)]

    my_graph = Graph_Matrix(nodes)
    my_graph.add_edges_from_list(edge_list)
    print(my_graph)
    return my_graph


def draw_undircted_graph(my_graph):  # 显示无向图
    G = nx.Graph()  # 建立一个空的无向图G
    for node in my_graph.vertices:
        G.add_node(str(node))
    for edge in my_graph.edges:
        G.add_edge(str(edge[0]), str(edge[1]))

    print("nodes:", G.nodes())  # 输出全部的节点： [1, 2, 3]
    print("edges:", G.edges())  # 输出全部的边：[(2, 3)]
    print("number of edges:", G.number_of_edges())  # 输出边的数量：1

    nx.draw(G, node_color='b', edge_color='r', with_labels=True)
    plt.savefig("undirected_graph.png")
    plt.show()


def draw_directed_graph(my_graph):  # 显示有向图，带权
    G = nx.DiGraph()  # 建立一个空的无向图G
    for node in my_graph.vertices:
        G.add_node(str(node))
    G.add_weighted_edges_from(my_graph.edges_array)

    print("nodes:", G.nodes())  # 输出全部的节点
    print("edges:", G.edges())  # 输出全部的边
    print("number of edges:", G.number_of_edges())  # 输出边的数量
    nx.draw(G, node_color='b', edge_color='r', with_labels=True)
    pos = spring_layout(G)
    plt.savefig("directed_graph.png")
    plt.show()
