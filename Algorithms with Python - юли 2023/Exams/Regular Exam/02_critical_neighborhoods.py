import heapq

def dijkstra_algo(graph, start, end, closed_roads):
    distances = {city: float('inf') for city in graph}
    distances[start] = 0

    paths = {city: [] for city in graph}
    paths[start] = [start]

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_city = heapq.heappop(priority_queue)

        if current_distance > distances[current_city]:
            continue

        for neighbor, weight in graph[current_city].items():
            if (current_city, neighbor) in closed_roads or (neighbor, current_city) in closed_roads:
                continue

            total_distance = distances[current_city] + weight
            
            if total_distance < distances[neighbor]:
                distances[neighbor] = total_distance
                paths[neighbor] = paths[current_city] + [neighbor]
                heapq.heappush(priority_queue, (total_distance, neighbor))

    return distances[end], paths[end]

def find_the_best_route(roads, closed_roads, start_city, end_city):
    graph = {}

    for road in roads:
        first_city, second_city, distance = road.split(' - ')
        distance = int(distance)

        if first_city not in graph:
            graph[first_city] = {}

        if second_city not in graph:
            graph[second_city] = {}

        graph[first_city][second_city] = distance
        graph[second_city][first_city] = distance

    closed_roads = set(tuple(road.split('-')) for road in closed_roads.split(','))

    distance, path = dijkstra_algo(graph, start_city, end_city, closed_roads)
    return distance, path

r = int(input())
roads = [input().strip() for _ in range(r)]

closed_roads = input().strip()
start_city = input().strip()
end_city = input().strip()

distance, path = find_the_best_route(roads, closed_roads, start_city, end_city)
print(' - '.join(path))
print(distance)
