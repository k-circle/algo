import heapq


def djikstra():
    graph = {
        'book': {
            'lp': 5,
            'poster': 0,
        },
        'lp': {
            'bass': 15,
            'drum': 20,
        },
        'poster': {
            'bass': 20,
            'drum': 35,
        },
        'bass': {
            'piano': 20,
        },
        'drum': {
            'piano': 10
        },
        'piano': {},
    }
    costs = {
        'book': 0,
        'lp': float('inf'),
        'poster': float('inf'),
        'bass': float('inf'),
        'drum': float('inf'),
        'piano': float('inf'),
    }
    visited = set()
    path = {
        'book': None,
    }
    while len(path) > len(visited):
        node = min({k: v for k, v in costs.items() if k not in visited}, key=costs.get)  # min cost in not visited nodes
        visited.add(node)
        for k, v in graph[node].items():
            if costs[k] > costs[node] + graph[node][k]:
                costs[k] = costs[node] + graph[node][k]
                path[k] = node
    end = 'piano'
    shortest_path = [end]
    while path[end]:  # calculate shortest path
        shortest_path.insert(0, path[end])
        end = path[end]
    print('Path:', ' -> '.join(shortest_path))
    print('Costs:', costs)


def djikstra_with_heap():
    graph = {
        'book': {
            'lp': 5,
            'poster': 0,
        },
        'lp': {
            'bass': 15,
            'drum': 20,
        },
        'poster': {
            'bass': 20,
            'drum': 35,
        },
        'bass': {
            'piano': 20,
        },
        'drum': {
            'piano': 10
        },
        'piano': {},
    }
    costs = {
        'book': 0,
        'lp': float('inf'),
        'poster': float('inf'),
        'bass': float('inf'),
        'drum': float('inf'),
        'piano': float('inf'),
    }
    q = [(k, v) for k, v in costs.items()]
    heapq.heapify(q)
    path = {
        'book': None,
    }
    while q:
        node = heapq.heappop(q)
        for k, v in graph[node[0]].items():
            if costs[k] > costs[node[0]] + graph[node[0]][k]:
                costs[k] = costs[node[0]] + graph[node[0]][k]
                heapq.heappush(q, (k, v))
                path[k] = node[0]
    end = 'piano'
    shortest_path = [end]
    while path[end]:  # calculate shortest path
        shortest_path.insert(0, path[end])
        end = path[end]
    print('Path:', ' -> '.join(shortest_path))
    print('Costs:', costs)


if __name__ == '__main__':
    djikstra()
    djikstra_with_heap()
