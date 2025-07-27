#declare variables
usr_input_str = []
usr_input_int = []
j=0
# class defination for Linked list creation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def add_element(element, data):
    tempnode = Node(data)
    if element is None:
        return tempnode
    
    lastnode = element
    while lastnode.next is not None:
        lastnode = lastnode.next
        
    lastnode.next = tempnode
    return element
    
def add_list(usr_input_int):
    element = None
    for data in usr_input_int:
        element = add_element(element, data)
    return element

def print_list(element):
    while element is not None:
        print(element.data, end=" ")
        element = element.next
        
def swap_list(input_list):
    if not input_list:
        return
    # Convert the input linked list to list type
    element = []
    templist = input_list
    while templist:
        element.append(templist.data)
        templist = templist.next
    for i in range (counthalf):
        j=i+1
        if( j % 2 == 0):
            #print (i,j,count-j+1, j//2)
            element[i], element[count-j] = element[count-j], element[i]
    # Convert the output list back to linked list format
    output_list = add_list(element)
    return output_list
    
# accept and validate input from user.
count = int(input("Enter the count of array elements: "))
counthalf = (count // 2)

# validate the counter value and number of elements are same.
usr_input = input("Enter the array elements seperated by spaces: ")
# split array
usr_input_str = usr_input.split()
usr_input_len = int(len(usr_input_str))
#print ("Raw input from user: ", usr_input)
#print ("User input converted to string array: ", usr_input_str)

#Conversion to Integer array
for element in usr_input_str:
    usr_input_int = usr_input_int + [int(element)]
#print ("User input converted to integer array: ",usr_input_int)

input_list = add_list(usr_input_int)
#print("\nList before swapping:")
#print_list(input_list)
#print("\n")
output_list = swap_list(input_list)
#print("List after swapping:")
print_list(output_list)



    

        



        