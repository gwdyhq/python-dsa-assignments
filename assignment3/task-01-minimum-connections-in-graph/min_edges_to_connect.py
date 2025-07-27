from collections import defaultdict

def func_find_conn(node, visited, graph):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            func_find_conn(neighbor, visited, graph)

def func_min_connection_req(test_cases):
    results = []
    for num_of_vertices, num_of_edges, edges in test_cases:
        graph = defaultdict(list)
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)

        visited = [False] * (num_of_vertices + 1)
        component_count = 0

        for i in range(1, num_of_vertices + 1):
            if not visited[i]:
                func_find_conn(i, visited, graph)
                component_count += 1

        min_edges_needed = component_count - 1

        if component_count == 1:
            results.append(0)
        elif component_count <= num_of_edges:
            results.append(min_edges_needed)
        else:
            results.append(-1)
    return results

# ---- Input handling ----
test_cases = []
num_of_test_cases = int(input("Enter the number of test cases: "))

for _ in range(num_of_test_cases):
    num_of_vertices, num_of_edges = map(int, input("Enter number of vertices and edges: ").split())
    edges = []
    print(f"Enter {num_of_edges} edge(s):")
    for _ in range(num_of_edges):
        u, v = map(int, input().split())
        edges.append((u, v))
    test_cases.append((num_of_vertices, num_of_edges, edges))

# ---- Output Results ----
output = func_min_connection_req(test_cases)
print("Minimum connections needed:")
for result in output:
    print(result)
