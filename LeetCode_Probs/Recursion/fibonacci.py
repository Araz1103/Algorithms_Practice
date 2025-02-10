# Recursive solution to get the nth Fibonacci Number

# F(N) = F(N-1) + F(N-2)
# F(1) = 1
# F(0) = 0


def get_fibonacci(n, num_operations):
    if n<=0:
        num_operations[0] +=1
        return 0
    elif n==1:
        num_operations[0] +=1
        return 1
    return get_fibonacci(n-1, num_operations) + get_fibonacci(n-2, num_operations)

for i in range(11):
    num_ops = [0]
    print(f"{i}th Fibonacci Number:", get_fibonacci(i, num_operations=num_ops))
    print("#NumOps", num_ops)
    print("-------------")

# Instead of Re-Calculating, can we store in memory and re-use values?
fibonacci_dict = {}
def get_fibonacci(n, num_operations):
    if n<=0:
        num_operations[0] +=1
        return 0
    elif n==1:
        num_operations[0] +=1
        return 1
    elif n in fibonacci_dict:
        # No operations here
        return fibonacci_dict[n]
    
    fibonacci_value = get_fibonacci(n-1, num_operations) + get_fibonacci(n-2, num_operations)
    # Store in dict to re-use
    fibonacci_dict[n] = fibonacci_value
    return fibonacci_value

print("Using Dict to store already computed values!")
i = 20
num_ops = [0]
print(f"{i}th Fibonacci Number:", get_fibonacci(i, num_operations=num_ops))
print("#NumOps", num_ops)
print(fibonacci_dict)

i = 30
num_ops = [0]
print(f"{i}th Fibonacci Number:", get_fibonacci(i, num_operations=num_ops))
print("#NumOps", num_ops)
print(fibonacci_dict)
# for i in range(11):
#     num_ops = [0]
#     print(f"{i}th Fibonacci Number:", get_fibonacci(i, num_operations=num_ops))
#     print("#NumOps", num_ops)
#     print("-------------")


# Using DP and Optimising for Space Complexity O(1)

def get_fibonacci_dp(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    
    dp_array = [0, 1]

    # If n is gt 1, then we basically get the next number by adding 2 previous
    for i in range(2, n+1):
        new_val = dp_array[0] + dp_array[1]
        # Update the array to include this value as the last one
        dp_array[0] = dp_array[-1] # Make the first element the current last element
        dp_array[-1] = new_val # Make the last element the new value
        # This way we use constant space O(1)

    return dp_array[-1] # The last value is our answer

print("Using DP!")
i = 20
print(f"{i}th Fibonacci Number:", get_fibonacci_dp(i))

i = 30
print(f"{i}th Fibonacci Number:", get_fibonacci_dp(i))
