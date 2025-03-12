class Solution:
    def reverseBits(self, n: int) -> int:
        # Reversing bits
        # 001101
        #   to
        # 101100

        # For each of the 32 bits
        # Right shift
        # If it is a 1
        # Make the final output end 1
        # If a 0, make the final output 0
        # Basically keep checking while the divided number doesn't become 0
        # Since then we know everything left is 0

        new_int = 0
        curr_power = 31
        # Basically starting @ 2^31
        # So keep adding to get new int value

        while n > 0:
            if n&1==1:
                # Last bit is 1
                # Use curr power to get sum and add to new int
                new_int += (2**curr_power)

            # Else we know we don't need to add anything to the new int    
            curr_power-=1
            # Discard right bit now
            n = n>>1

        return new_int
    
# More Optimised Soln, Code wise cleaner and not using **
# Though technically both above and this is O(1)
def reverseBits(n: int) -> int:
    new_int = 0
    for _ in range(32):  # Iterate through all 32 bits
        new_int = (new_int << 1) | (n & 1)  # Shift left and add the rightmost bit of n
        n >>= 1  # Shift n right
    return new_int