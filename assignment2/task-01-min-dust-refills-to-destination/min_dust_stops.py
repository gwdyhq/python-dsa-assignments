import ast
dest_miles = int(input("Enter destination miles: "))
available_dust = int(input("Enter dust available at start: "))
input_list = input("Enter the list of stop_count: ")
wells_list = ast.literal_eval(input_list)
max_list = ast.literal_eval(input_list)
start_point = 0
stop_count = 0
#wells_list = [[5, 10], [10, 6], [12, 100]]
#wells_list.append([0,5])
wells_list.append([dest_miles,0])
count = len(wells_list)
#print (wells_list)
dust_required = []

# Traverse the list of wells to create a max heap
def function_max_dust_heap(max_list,count,i):
    # parent,left and right nodes
    max_dust = i
    left_dust = 2*i + 1 # left child of the parent
    right_dust = 2*i + 2 # right child of the parent

    #comparing the list elements to form a max heap
    if left_dust < count and max_list[left_dust][1] > max_list[max_dust][1]:
        max_dust = left_dust
        #print (max_dust,left_dust)

    if right_dust < count and max_list[right_dust][1] > max_list[max_dust][1]:
        max_dust = right_dust
        #print (max_dust,right_dust)

    if max_dust != i:
        max_list[i],max_list[max_dust] = max_list[max_dust],max_list[i]
        #print (wells_list)
        
        #call function again to compare other members.
        function_max_dust_heap(max_list,count,max_dust)
    

#print (wells_list)

count1 = len(max_list)
k = int(count1 / 2) - 1
while k >= 0:
    function_max_dust_heap(max_list, count1, k)
    k = k - 1

k = count1 - 1
while k >= 0:
    max_list[0], max_list[k] = max_list[k], max_list[0]
    function_max_dust_heap(max_list, k, 0)
    k = k - 1

def function_reach_destination(dest_miles, available_dust, wells_list, start_point, stop_count, dust_required):
    
    for wells in wells_list:
        
        
        distance_travelled = wells[0] - start_point
        
        distance_left = dest_miles - start_point
        
        i = j = 0
        
        #print (distance_travelled,distance_left)
        
        while distance_travelled > available_dust:
            
            if len(dust_required) == 0:
                return -1  
            
            max_dust = max(dust_required)
            
            available_dust = available_dust + max_dust
            
            stop_count = stop_count + 1
            
            dust_required.remove(max_dust)
        
        start_point = wells[0]
        
        distance_left = dest_miles - start_point
        
        available_dust = available_dust - distance_travelled
        
        dust_required.append(wells[1])

    
    while distance_left > available_dust:
        
        if len(dust_required) == 0:
            return -1  
        
        max_dust = max(dust_required)
        
        available_dust = available_dust + max_dust
        
        stop_count = stop_count + 1
        
        dust_required.remove(max_dust)

    return stop_count


num_of_halts = function_reach_destination(dest_miles, available_dust, wells_list, start_point, stop_count, dust_required)

print (num_of_halts)


   



