#  / B --- D \
#A      /  |   F
#  \ C --- E

def DFS(graph, start):
    stack = []
    seen = set()
    stack.append(start)
    seen.add(start)
    while(stack):
        tmp = stack.pop(-1)
        vertex = graph[tmp]
        print(tmp)
        for v in vertex:
            if v not in seen:
                stack.append(v)
                seen.add(v)


if __name__ == "__main__":
    graph = { "A" : ["B", "C"],
              "B" : ["A", "D"],
              "C" : ["A", "D", "E"],
              "D" : ["B", "C", "E", "F"],
              "E" : ["C", "D"],
              "F" : ["D"]}
    DFS(graph, "E")
