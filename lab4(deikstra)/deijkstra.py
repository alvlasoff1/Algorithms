
def find_way(graph: dict, start):
    costs_par = {start: [start, 0]}
    procceded = [start, ]
    for child in graph[start]:
        costs_par[child] = [start, graph[start][child]]
    for child in graph:
        if child not in costs_par and child != start:
            costs_par[child] = [None, float('inf')]

    def find_lowest(costs):
        ans = None
        min_num = float('inf')
        for key, value in costs.items():
            if value[1] < min_num and key not in procceded:
                min_num = value[1]
                ans = key
        return ans
    node = find_lowest(costs_par)
    while node and node not in procceded:
        cost = costs_par[node][1]
        for child in graph[node]:
            new_cost = cost + graph[node][child]
            if costs_par[child][1] > new_cost:
                costs_par[child][0] = node
                costs_par[child][1] = new_cost
        procceded.append(node)
        node = find_lowest(costs_par)


    return costs_par


my_graph = {
    "Green Park": {"Oxford Circus": 1, "Bond Street": 1, "Piccadily circus": 2},
    "Bond Street": {"Oxford Circus": 1, "Baker street": 3},
    "Piccadily circus": {"Oxford Circus": 3, "Leicester square": 1},
    "Oxford Circus": {"Regent's Park": 2, "Warren street": 4, "Tottenham Court road": 2},
    "Regent's Park": {"Baker street": 2},
    "Baker street": {"Warren street": 2},
    "Warren street": {"Goodge street": 3},
    "Goodge street": {"Tottenham Court road": 1},
    "Tottenham Court road": {"Holboran": 2},
    "Leicester square": {"Tottenham Court road": 1, "Holboran": 2},
    "Holboran": {}
}

#print(find_way(my_graph, "Green Park"))