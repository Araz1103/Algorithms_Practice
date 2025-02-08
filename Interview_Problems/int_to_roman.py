"""
Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.

 

Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
Example 2:

Input: num = 58

Output: "LVIII"

Explanation:

50 = L
 8 = VIII
Example 3:

Input: num = 1994

Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV
 

Constraints:

1 <= num <= 3999
"""

class Solution(object):
    # Approach
    # 1, 2, 3 is repeating
    # 4 is 1 less
    # 5 has a symbol
    # 6, 7, 8 is increasing with 5 ( repeating the unit's symbol)
    # 9 is 1 less

    # Now depending on the decimal place, the above are followed with different symbols

    def get_representation(self, num, place):
        # Num is the single digit between 0 - 9
        if place == 4: #Decimal Place for Thousand
            if num in [1, 2, 3]: # For our scope it's not beyond this
                return "M"*num

        elif place == 3: #Decimal Place for Hundreds
            if num == 0:
                return "" #No value, as it's coming from the previous one
            elif num in [1, 2, 3]:
                return "C"*num
            elif num == 4:
                return "CD"
            elif num == 5:
                return "D"
            elif num in [6, 7, 8]:
                return "D" + "C"*(num - 5)
            else: #num is 9
                return "CM"

        elif place == 2: #Decimal Place for Tens
            if num == 0:
                return "" #No value, as it's coming from the previous one
            elif num in [1, 2, 3]:
                return "X"*num
            elif num == 4:
                return "XL"
            elif num == 5:
                return "L"
            elif num in [6, 7, 8]:
                return "L" + "X"*(num - 5)
            else: #num is 9
                return "XC"

        else: #Decimal Place for Ones
            if num == 0:
                return "" #No value, as it's coming from the previous one
            elif num in [1, 2, 3]:
                return "I"*num
            elif num == 4:
                return "IV"
            elif num == 5:
                return "V"
            elif num in [6, 7, 8]:
                return "V" + "I"*(num - 5)
            else: #num is 9
                return "IX"
            
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_reprs = ""
        num_len = len(str(num))
        for digit in str(num):
            roman_reprs += self.get_representation(int(digit), num_len)
            num_len -=1

        return roman_reprs

        