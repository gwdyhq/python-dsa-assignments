import collections
from collections import Counter
# Declare variables for the program.
usr_input = []
usr_input_str = []
usr_input_int = []
count = 0
removednum = 0
removedcount = 0

# accept and validate input from user.
count = int(input("Enter the count of array elements: "))

# validate the counter value and number of elements are same.

usr_input = input("Enter the array elements seperated by spaces: ")
# split array
usr_input_str = usr_input.split()
usr_input_len = int(len(usr_input_str))
counthalf = (usr_input_len // 2)
rem = (usr_input_len % 2)
#print (rem)
#print (counthalf)

#Conversion to Integer array
for i in usr_input_str:
    usr_input_int = usr_input_int + [int(i)]
#print ("User input converted to integer array: ",usr_input_int)

#Find occurence of repeated elements
repeat_count = Counter(usr_input_int)
#print ("Elements along with their repetition value: ",repeat_count)

#Get repetition values for each element and sort them in decending order.
repeat_array = sorted(repeat_count.values(), reverse = True)
#print ("Repetition values: ", repeat_array)

#Reduce the array by removing repeated elements
#Remove repeated elements until array size reaches half of its original size
for j in repeat_array:
    removednum = removednum + j
    removedcount = removedcount + 1
    if (rem==0):
        if (removednum >= counthalf):
            break
    else:
        if (removednum > counthalf):
            break
    
#print ("Count of elements removed: ",removednum)
#print ("\n*************************************************************************************")
#print ("*************************************************************************************\n")
print (removedcount)
#print ("\n*************************************************************************************")
#print ("*************************************************************************************")





