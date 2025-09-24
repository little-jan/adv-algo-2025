def find_max(vertex_weights, edges):   # vertex_weights is list, edges is key-value pairs (key is src, value is v)
    final_costs = [0 for _ in vertex_weights]

    for i in range(len(vertex_weights)):
        edge = i + 1
        while True:
            if edge not in edges:
                break
            else:
                if final_costs[edge - 1] == 0:
                    v_weight = edges[edge]
                    final_costs[edge - 1] = v_weight
                else:
                    v_weight = edges[edge]
                    if v_weight > final_costs[edge - 1]:
                        final_costs[edge - 1] = v_weight
                edge = edges[edge]

    return final_costs

vertices, num_edges = input().split()
vertices, num_edges = int(vertices), int(num_edges)

vertex_weights = []
for i in range(vertices):
    vertex_weights.append(int(input()))

edges = {}
for j in range(num_edges):
    key, value = input().split()
    key, value = int(key), int(value)
    edges[key] = value

final_costs = find_max(vertex_weights, edges)
for val in final_costs:
    print(val)