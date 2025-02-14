"""
Watson likes to challenge Sherlock's math ability. He will provide a starting and ending value that describe a range of integers, inclusive of the endpoints. Sherlock must determine the number of square integers within that range.
Note: A square integer is an integer which is the square of an integer, e.g. .
Example


There are three square integers in the range:  and . Return .
Function Description
Complete the squares function in the editor below. It should return an integer representing the number of square integers in the inclusive range from  to .
squares has the following parameter(s):
int a: the lower range boundary
int b: the upper range boundary
Returns
int: the number of square integers in the range
Input Format
The first line contains , the number of test cases.
Each of the next  lines contains two space-separated integers,  and , the starting and ending integers in the ranges.
Constraints

1 <=a<=b<=10**9

Sample Input
2
3 9
17 24
Sample Output
2
0
Explanation
Test Case #00: In range ,  and  are the two square integers.
Test Case #01: In range , there are no square integers.
"""

def squares(a, b):
    # Iterative approach
    # Iterate through a to b
    # if num**(0.5) is a whole number, then it is a perfect square
    # But this will be O(N)

    # Can we think better?
    # So if a num's square exceeds the range
    # This means that all the square's in the range were before this
    # So can count from there

    # So for range [a, b]
    # Start from a, and keep checking until the square of that number exceeds b
    # Basically all the numbers between a and b are squares of some numbers until x and y
    # x is integer <= sqrt of a
    # so starting from x, keep squaring and checking if sqr > b
    # if sqr > b, stop
    num_squares_set = set()
    sqrt_int_a = int(a**0.5)
    if float(sqrt_int_a) == a**0.5:
        num_squares_set.add(a) 

    check_num = sqrt_int_a + 1
    square = check_num**2
    while square <= b:
        num_squares_set.add(square)
        check_num +=1
        square = check_num**2

    return num_squares_set

    # for num in range(a, b+1):
    #     # Check if it is in num squares or not
    #     if num not in num_squares_set:
    #         sqr_root = num**(0.5)
    #         if (sqr_root == float(int(sqr_root))):
    #             num_squares_set.add(num)
            
    #         num_square = num**2
    #         if num_square <= b:
    #             num_squares_set.add(num_square)
    #         else:
    #             # Till now we will have all the squares
    #             break

    #     else:
    #         # If already in set, just check if the square in range or not
    #         num_square = num**2
    #         if num_square <= b:
    #             num_squares_set.add(num_square)
    #         else:
    #             # Till now we will have all the squares
    #             break

    return list(num_squares_set)

num = 36**(0.5)
print(num)
print(num == float(int(num)))

num = 37**(0.5)
print(num)
print(num == float(int(num)))

print(squares(0,0))
print(squares(1,10**2))
print(squares(1, 10**4))
print(squares(35, 70))