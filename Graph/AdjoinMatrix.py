# 邻接矩阵
'''

a---b\
|  | \
|  | c
|  | /
e---d/

对于无向图顶点之间存在边,则为1,反之则为0

 a b c d e
a 0 1 0 0 1
b 1 0 1 1 0
c 0 1 0 1 0
d 0 1 1 0 1
e 1 0 0 1 0

观察得知对脚线对称

对于有向图,若a--->b存在,则为ab之间为1,ba为0
对于有权值的存在,可以设置相应的数值

缺陷:
1.对于定点多边少的图,构造的矩阵空间浪费
2.获取某个顶点的邻接顶点,需要遍历相应的列表,找到1的顶点

'''
def addEdge1(graph, NodeA, NodeB):
    """
        undirected graph
    """
    graph[NodeA][NodeB] = 1
    graph[NodeB][NodeA] = 1

def addEdge2(graph, NodeA, NodeB):
    """
        directed graph
        NodeA to NodeB
    """
    graph[NodeA][NodeB] = 1

if __name__ == "__main__":
    N = 5 #Node number
    a,b,c,d,e = range(N)
    graph = [[0]*N for _ in range(N)]
    addEdge1(graph,a,b)
    addEdge1(graph,c,e)
    addEdge1(graph,e,a)
