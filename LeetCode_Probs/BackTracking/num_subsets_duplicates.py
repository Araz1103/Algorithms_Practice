# To count num distinct subsets in case of duplicates
# Intuition
# 1, 1, 2, 3, 3, 4, 4, 4
# Normally for each element, 2 choices, include it or not
# So 2^N choices
# Now to avoid duplicate subsets, let's consider all unique elements independently
# Element Frequency
#   1:      2
#   2:      1
#   3:      2
#   4:      3

# For each of these, we have frequency + 1 choices
# For 1: include it 0, 1 or 2 times
# For 2: include it 0 or 1 times
# For 3: include it 0, 1 or 2 times
# For 4: include it 0, 1, 2 or 3 times

# So num choices: 3*2*3*4


