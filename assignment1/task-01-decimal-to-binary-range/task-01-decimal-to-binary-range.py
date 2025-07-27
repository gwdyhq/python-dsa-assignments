# function to accept decimal input and convert to binary
def binary_calc(integer):
    binary_output = ''
    while integer > 0:
        temp = integer
        integer = integer//2
        binary_output = str(temp%2) + binary_output
    return binary_output

#function to get range of decimal numbers from the integer provided and call the conversion function to convert them into binary        
def get_binary_num(num):
    final_output = ''
    for integer in range(num1+1):
        binary_output = binary_calc(integer)
        final_output += binary_output + ' ' 
    return final_output

decimal_input = []
# Accept number of test cases to be executed
count = int(input("Enter test case count: "))
# Accept integers one by one for binary conversion
for num in range(count):
    decimal_input.append(int(input('Enter decimal integers: ')))
    
for num1 in decimal_input:
    final_output = get_binary_num(num)
    print (final_output)

