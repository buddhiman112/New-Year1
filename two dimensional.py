# Creating a 2D list
##two_dim_list = [
##    [1, 2, 3],
##    [4, 5, 6],
##    [7, 8, 9]
##]
##
### Accessing elements
##print(two_dim_list[0][0])  # Accessing the element at row 0, column 0 (output: 1)
##print(two_dim_list[1][2])  # Accessing the element at row 1, column 2 (output: 6)
##print(two_dim_list[2][1])  # Accessing the element at row 2, column 1 (output: 8)
##
### Modifying elements
##two_dim_list[1][1] = 99
##print(two_dim_list[1][1])  # After modification (output: 99)
##
### Iterating over rows
##for row in two_dim_list:
##    print(row)
##
### Iterating over all elements
##for row in two_dim_list:
##    for element in row:
##        print(element, end=' ')
##    print()  # Printing a newline after each row

##my_tuple = (1, 2, 3, 2)
##print(len(my_tuple(1)))  # Output: 1 (index of first occurrence of 2)
####
##my_tuple = (1, 2, 3, 4, 5)


######print(my_tuple[1:4])  # Output: (2, 3, 4)
####
####
####my_tuple = (1, 2, 3)
####print(2 in my_tuple)  # Output: True
####
####tuple1 = (1, 2)
####tuple2 = (3, 4)
####concatenated_tuple = tuple1 + tuple2
####print(concatenated_tuple)  # Output: (1, 2, 3, 4)
####
####repeated_tuple = (5 ,) * 3
####print(repeated_tuple)  # Output: (5,5,5)
####
my_tuple = (100, 2, 3)
print(my_tuple[0])  # Output: 100
