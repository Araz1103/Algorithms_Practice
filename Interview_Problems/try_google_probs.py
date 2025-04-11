from typing import List, Optional

# =====================
# Question 1: Package Delivery via Flights
# =====================

def can_package_reach_destination(origin, destination, flights):
    """
    Determine whether a package can be transferred from the origin to the destination
    using a list of available flights. Each flight is defined by its departure airport,
    arrival airport, departure time, and arrival time.

    The package starts at the origin airport at time 0. It can take a flight only if the
    departure time of the flight is greater than or equal to the arrival time of the package
    at the departure airport. There are no layover constraints other than timing.

    The goal is to determine whether the package can eventually reach the destination airport
    following valid flight paths in chronological order.

    Parameters:
        origin (str): The starting airport (e.g., "NYC")
        destination (str): The target airport (e.g., "SFO")
        flights (List[Tuple[str, str, int, int]]): Each tuple represents a flight with:
            - departure_airport (str)
            - arrival_airport (str)
            - departure_time (int)
            - arrival_time (int)

    Returns:
        bool: True if the package can reach the destination, False otherwise.
    """
    pass  # Your implementation here

# Test cases for Question 1
flights1 = [
    ("NYC", "LAX", 0, 4),
    ("LAX", "SFO", 5, 7)
]
assert can_package_reach_destination("NYC", "SFO", flights1) == True

flights2 = [
    ("NYC", "LAX", 0, 4),
    ("LAX", "SFO", 3, 5)
]
assert can_package_reach_destination("NYC", "SFO", flights2) == False

flights3 = [
    ("A", "B", 1, 2),
    ("B", "C", 3, 4),
    ("C", "D", 5, 6)
]
assert can_package_reach_destination("A", "D", flights3) == True

flights4 = [
    ("A", "B", 1, 2),
    ("B", "C", 2, 3),
    ("C", "D", 3, 4)
]
assert can_package_reach_destination("A", "D", flights4) == True

flights5 = [
    ("A", "B", 1, 2),
    ("B", "C", 1, 2),
    ("C", "D", 3, 4)
]
assert can_package_reach_destination("A", "D", flights5) == False


# =====================
# Question 2: Simplify Expression with +, -, and Parentheses
# =====================

def simplify_expression(expr):
    """
    Simplify an algebraic expression containing lowercase variables (a-z),
    plus and minus signs, and parentheses that are only one level deep (no nesting).

    The goal is to return a simplified expression by distributing signs and combining
    like terms (i.e., variables with the same name), outputting the final result as a
    string in standard form.

    Assumptions:
    - No multiplication or division involved.
    - Input is guaranteed to be valid and properly formatted.
    - White spaces may or may not be present in the input string.

    Example:
        Input: "a+b+a+c-b-b-b+(d+c)"
        Output: "2a-2b+2c+d"

    Parameters:
        expr (str): The expression string to simplify

    Returns:
        str: Simplified expression string with like terms combined and signs handled
    """
    pass  # Your implementation here

# Test cases for Question 2
assert simplify_expression("a+b+a+c-b-b-b+(d+c)") == "2a-2b+2c+d"
assert simplify_expression("x+y-(x-y)+z") == "2y+z"
assert simplify_expression("a-(b+c)+d") == "a-b-c+d"
assert simplify_expression("m+n-(p+q-r)") == "m+n-p-q+r"
assert simplify_expression("a-a+(b-b)+(c+c)-d") == "2c-d"


# =====================
# Question 3: Find the nth License Plate
# =====================

def get_nth_license_plate(n):
    """
    Given an integer n, return the nth license plate in lexicographical order using a custom encoding.

    License plate rules:
    - All license plates are of length 5
    - Characters used are 0-9 followed by A-Z (base-36 system)
    - The order starts from "00000" → "00001" → ... → "99999" → "0000A" → ... → "ZZZZZ"

    Examples:
        get_nth_license_plate(0) => "00000"
        get_nth_license_plate(1) => "00001"
        get_nth_license_plate(3) => "00003"
        get_nth_license_plate(36) => "00010"
        get_nth_license_plate(1295) => "000ZZ"
        get_nth_license_plate(1296) => "00100"

    Parameters:
        n (int): the index of the license plate (0-indexed)

    Returns:
        str: a 5-character license plate string
    """
    pass  # Your implementation here

# Test cases for Question 3
assert get_nth_license_plate(0) == "00000"
assert get_nth_license_plate(1) == "00001"
assert get_nth_license_plate(35) == "0000Z"
assert get_nth_license_plate(36) == "00010"
assert get_nth_license_plate(1295) == "000ZZ"
assert get_nth_license_plate(1296) == "00100"
assert get_nth_license_plate(36**5 - 1) == "ZZZZZ"


"""
Problem 4: Maximum Subarray Sum (Kadane’s Algorithm)
-----------------------------------------------------

Given a list of integers `nums`, return the maximum sum of any contiguous subarray.
This is a classic application of Kadane’s Algorithm.

Examples:
>>> max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
6  # Subarray [4, -1, 2, 1]
"""
def max_subarray_sum(nums: List[int]) -> int:
    pass

# Problem 4
assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert max_subarray_sum([5, 4, -1, 7, 8]) == 23
assert max_subarray_sum([-1, -2, -3]) == -1
assert max_subarray_sum([1, 2, 3, -2, 5]) == 9


"""
Problem 5: Max Subarray Sum with Matching Ends
----------------------------------------------

Given a list of integers `nums`, find the indices `[i, j]` such that:
- The subarray nums[i] + nums[i+1] + ... + nums[j] has the maximum sum
- And nums[i] == nums[j]

Return the pair [i, j].

Examples:
>>> max_subarray_sum_with_ends_equal([1, 3, 5, 6, 3, -6, 3])
[1, 4]  # Subarray is [3, 5, 6, 3]
"""
def max_subarray_sum_with_ends_equal(nums: List[int]) -> List[int]:
    pass

# Problem 5
assert max_subarray_sum_with_ends_equal([1, 3, 5, 6, 3, -6, 3]) == [1, 4]
assert max_subarray_sum_with_ends_equal([2, 1, 2, -1, 2, 3, 2]) == [0, 6]
assert max_subarray_sum_with_ends_equal([1, 2, 3, 2, 1]) == [1, 3]


"""
Problem 6: Subset Sum Less Than or Equal to K
---------------------------------------------

You're given a list of integers `nums` and a number `k`. Find the maximum sum
that can be formed from any subset of `nums` such that the sum is <= k.

Examples:
>>> subset_sum_leq_k([2, 1, 3, 4], 5)
5  # 2 + 3 or 1 + 4
>>> subset_sum_leq_k([10, 20, 30], 15)
10
"""
def subset_sum_leq_k(nums: List[int], k: int) -> int:
    pass

# Problem 5
assert subset_sum_leq_k([2, 1, 3, 4], 5) == 5
assert subset_sum_leq_k([10, 20, 30], 15) == 10
assert subset_sum_leq_k([1, 2, 3, 4, 5], 11) == 11
assert subset_sum_leq_k([7, 10, 4], 8) == 7

"""
Problem 6: Infix Notation Conversion & Minimization
---------------------------------------------------

Part A: Convert an infix expression (e.g. "a+(b*c)") to postfix (RPN) format.
Part B: Minimize parentheses while preserving the expression’s evaluation order.

Examples:
>>> infix_to_postfix("a+(b*c)")
"abc*+"
>>> minimize_brackets("((a+b))")
"a+b"
>>> minimize_brackets("a+(b*(c+d))")
"a+b*(c+d)"
"""
def infix_to_postfix(expression: str) -> str:
    pass

def minimize_brackets(expression: str) -> str:
    pass







# Problem 6
assert infix_to_postfix("a+(b*c)") == "abc*+"
assert infix_to_postfix("a+b*(c^d-e)^(f+g*h)-i") == "abcd^e-fgh*+^*+i-"

assert minimize_brackets("((a+b))") == "a+b"
assert minimize_brackets("a+(b*(c+d))") == "a+b*(c+d)"
assert minimize_brackets("((a+(b)))") == "a+b"
assert minimize_brackets("((a+b)*(c-d))") == "(a+b)*(c-d)"