def max_num(one, two, three):
    # Write a Python function called max_num()to find the maximum of three numbers.
    return max([one, two, three])

print(max_num(4, 3, 6)) # 6

def mult_list(lst):
    # Write a Python function called mult_list() to multiply all the numbers in a list.
    if len(lst) == 0:
        return 0
    
    result = lst[0]

    if len(lst) > 1:
        for i in lst[1:]:
            result = result * i

    return result

print(mult_list([4, 2, 2])) # 16

def rev_string(string):
    # Write a Python function called rev_string() to reverse a string.
    return string[::-1]

print(rev_string("taco")) # acot

def num_within(i, min, max):
    # Write a Python function called num_within() to check whether a number falls in a given range.
    return i in range(min, max + 1)

print(num_within(4, 2, 5)) # True

# PASCAL
triangle = [[1], [1, 1]]
def pascal(n):
    #Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
    if n < 1:
        print("Invalid number of rows")
    elif n == 1:
        print(triangle[0])
    else: 
        row_number = 2
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            length = len(row_prev) + 1

            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length - 1:
                    row.append(triangle[row_number - 1][i - 1] + triangle[row_number - 1][i])
                else: 
                    row.append(1)

            triangle.append(row)
            row_number += 1

        for row in triangle:
            print(row)

pascal(3)