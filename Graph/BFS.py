#  / B --- D \
#A      /  |   F
#  \ C --- E

def BFS(graph, start):
    queue = []
    seen = set()
    queue.append(start)
    seen.add(start)    # 走过的不走
    while(queue):
        tmp = queue.pop(0)
        print(tmp)
        vertex = graph[tmp]
        for v in vertex:
            if v not in seen:
                seen.add(v)
                queue.append(v)

if __name__ == "__main__":
    graph = { "A" : ["B", "C"],
              "B" : ["A", "D"],
              "C" : ["A", "D", "E"],
              "D" : ["B", "C", "E", "F"],
              "E" : ["C", "D"],
              "F" : ["D"]}
    BFS(graph, "E")
