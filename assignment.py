def max_num(one, two, three):
    # Write a Python function called max_num()to find the maximum of three numbers.
    return max([one, two, three])

print(max_num(1,2,3))
print(max_num(100,50,1))
print(max_num(15,30,2))

def mult_list(lst):
    # Write a Python function called mult_list() to multiply all the numbers in a list.
    if len(lst) == 0:
        return 0
    
    result = lst[0]

    if len(lst) > 1:
        for i in lst[1:]:
            result = result * i

    return result

print(mult_list([1,2,3]))
print(mult_list([]))
print(mult_list([15]))

def rev_string(string):
    # Write a Python function called rev_string() to reverse a string.
    return string[::-1]

print(rev_string(""))
print(rev_string("apple"))
print(rev_string("mt string"))

def num_within(i, min, max):
    # Write a Python function called num_within() to check whether a number falls in a given range.
    return i in range(min, max + 1)

print(num_within(3,2,4))     
print(num_within(3,1,3))     
print(num_within(10,2,5))

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

pascal(2)
pascal(5)