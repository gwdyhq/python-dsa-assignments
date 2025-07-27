#import required libraries
import ast

#define variables
visit_list =  []
visit_list1 =  []
visit_list2 =  []

#read inputs from user
num_of_cities = int(input("Enter the number of cities to visit: "))
visit_list1 = input("Enter visit details in order fromcity,tocity,cost: ")
visit_list2 = ast.literal_eval(visit_list1)
for each_list in visit_list2:
    visit_list = visit_list + [each_list]
start_city = int(input("Enter the start city: "))
dest_city = int(input("Enter the destination city: "))
max_stops = int(input("Enter the maximum stops: "))

#deifne merge sort array function for sorting the list in ascending order
def func_merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[0:mid]
        right_half = arr[mid:len(arr)]

        func_merge_sort(left_half)
        func_merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][0] < right_half[j][0]:
                arr[k] = left_half[i]
                i = i + 1
            else:
                arr[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i = i + 1
            k =k + 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j =j + 1
            k = k + 1

#define function to calculate the least cost between the 2 stops
def func_least_travel_cost(n, trains, start, end, max_stops):
    # Create the adjacency list
    graph = {i: [] for i in range(n)}
    for travel in trains:
        start_city = travel[0]
        dest_city = travel[1]
        cost = travel[2]
        graph[start_city].append((dest_city, cost))
        graph[dest_city].append((start_city, cost))

    # Priority queue to store (cost, current_city, stops)
    queue1 = [(0, start, 0)]
    # Dictionary to store the minimum cost to reach each city with a certain number of stops
    costs = {(start, 0): 0}

    while queue1:
        # Find the element with the minimum cost using merge sort
        func_merge_sort(queue1)
        #cost, city, stops = queue1.pop(0)
        first_element = queue1[0]
        queue1 = queue1[1:]
        cost = first_element[0]
        city = first_element[1]
        stops = first_element[2]
        # If we reached the destination and within the stop limit
        if city == end:
            return cost
        # If we have more stops left
        if stops <= max_stops:
            for next_travel in graph[city]:
                next_city = next_travel[0]
                next_cost = next_travel[1]
                new_cost = cost + next_cost
                # If we have not visited this city with this number of stops, or found a cheaper way
                if (next_city, stops + 1) not in costs or new_cost < costs[(next_city, stops + 1)]:
                    costs[(next_city, stops + 1)] = new_cost
                    queue1.append((new_cost, next_city, stops + 1))

    # If we exhaust the priority queue without finding the destination
    return -1

print(func_least_travel_cost(num_of_cities, visit_list, start_city, dest_city, max_stops)) 
#[[1, 2, 20], [1, 3, 10], [1, 6, 30], [2, 5, 40], [3, 4, 50], [4, 5, 60], [5, 6, 70], [0, 1, 22]]
