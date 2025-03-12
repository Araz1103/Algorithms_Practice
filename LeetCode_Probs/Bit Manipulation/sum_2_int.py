# class Solution {
#     public int getSum(int a, int b) {
#         while (b!=0) {
#             int carry = (a & b) << 1;
#             a = a^b;
#             b = carry;
#         }
#         return a;
#     }
# }

# In python this breaks, that's why did in Java
class Solution:
     def getSum(self, a: int, b: int) -> int:
        while b!=0: #Using b as carry
            a_and_b = (a&b)<<1
            a = a^b
            b = a_and_b #Carry
            # So if carry is non zero, we again add a and b (carry)
            # Once finished, when b/carry is zero, ans is in a
        return a