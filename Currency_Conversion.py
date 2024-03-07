conversionList = [
    ("A", "B", 1.1), ("A", "C", 2.1), ("A", "D", 2.64),
    ("B", "C", 2.0), ("B", "D", 2.4), ("B", "E", 4.0),
    ("C", "E", 2.0), ("C", "D", 1.26), ("F", "C", 3.0),
    ("D", "E", 2.7), ("F", "G", 2.0)
]

def calculateConversion(source, destination, conversionList):

    graph = defaultdict(list)

    for conv in conversionList:
        graph[conv[0]].append((conv[1], conv[2]))
    
    def dfs(curr, destination, graph, visited, path, rate):
        if curr == destination:
            return path + [curr], rate
        
        visited.add(curr)
        for neighbor, factor in graph[curr]:
            if neighbor not in visited:
                new_path = path + [curr]
                new_rate = rate * factor
                res_path, res_rate = dfs(neighbor, destination, graph, visited, new_path, new_rate)
                if res_path:
                    return res_path, res_rate
        return None, None

    
    # initialization
    visited = set()
    path, rate = dfs(source, destination, graph, visited, [], 1)

    if path:
        return path, rate
    else:
        "No conversion route found."

print(calculateConversion("A", "E", conversionList))