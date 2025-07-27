popularity_index = []
output = ''
k = 0

num_of_books = int(input("Enter number of books: "))
popularity_input = input("Enter the array elements seperated by spaces: ")

popularity_index = popularity_input.split()

for i in range(num_of_books):
    count = 0
    popularity_index_temp = popularity_index[i+1:]
    #print (min(popularity_index_temp))
    count = [count + 1 if int(index) < int(popularity_index[i]) else count for index in popularity_index_temp]
    if (k < num_of_books):
        output = output + str(sum(1 for j in count if j > 0)) + ' '
        k += 1
    else:
        output = output + str(sum(1 for j in count if j > 0))
print (output)


    
