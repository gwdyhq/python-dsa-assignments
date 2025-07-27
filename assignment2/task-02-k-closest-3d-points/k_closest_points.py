import ast
N = int(input("Number of 3D points: "))
K = int(input("Number of close points to be found: "))
input_list = input("list of all points: ")
list_of_points = ast.literal_eval(input_list)
#N = 3
#K = 2
#list_of_points = [[-6, -9, -4], [6, -2, 0], [-5, -4, 2]]
distance_list = []
list_of_close_points = []
i = 0
j = 0
k = 0

def is_not_equal(i, j):
    return i != j

# Function to get max heap
def function_heapify(distance_list, count, i):
    max_i = i
    
    left_i = 2 * i + 1
    
    right_i = 2 * i + 2
    
    #left_element = distance_list[left_i]
    #right_element = distance_list[right_i]
    #max_element = distance_list[max_i]

    if left_i < count and distance_list[left_i][0] > distance_list[max_i][0]:
        max_i = left_i

    if right_i < count and distance_list[right_i][0] > distance_list[max_i][0]:
        max_i = right_i

    if is_not_equal(i, max_i):
        distance_list[i], distance_list[max_i] = distance_list[max_i], distance_list[i]
        #recursive call to heapify all elements
        function_heapify(distance_list, count, max_i)

# Main code begins here
# Find euclidean distance for each point
while i < len(list_of_points):
    
    #print (list_of_points[i][0],list_of_points[i][1],list_of_points[i][2])
    
    point1 = list_of_points[i][0]
    
    point1_dis = point1**2
    
    point2 = list_of_points[i][1]
    
    point2_dis = point2**2
    
    point3 = list_of_points[i][2]
    
    point3_dis = point3**2
    
    euclidean_distance = point1_dis + point2_dis + point3_dis
    
    #print (point1_dis,point2_dis,point3_dis,euclidean_distance)

    distance_list.append([euclidean_distance, list_of_points[i]])

    i = i + 1

#print(distance_list)
   
# sort the points based of their euclidean distance
count = len(distance_list)

j = int(count / 2) - 1

while j >= 0:
    
    function_heapify(distance_list, count, j)
    
    j = j - 1


j = count - 1


while j >= 0:
    
    distance_list[0], distance_list[j] = distance_list[j], distance_list[0]
    
    function_heapify(distance_list, j, 0)
    
    j = j - 1


#print(distance_list)
j = 0
# Find the close points
while j < K:

    list_of_close_points.append(distance_list[j][1])

    j = j + 1
    
print (list_of_close_points)