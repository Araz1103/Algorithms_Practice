
def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    # d1, m1, y1: Return Date
    # d2, m2, y2: Due Date
    # To calculate fine
    # If before or on due date: 0
    # If returned in same month: 15*(#num days late)
    # If returned in same year: 500*(#num months late)
    # If returned post same year: fixed 10,000

    # First check Year
    # Then month
    # Then day

    if y1 > y2:
        return 10000
    elif y1 < y2:
        return 0 #Returning any year before, is ok!
    
    if m1 > m2:
        return 500*(m1-m2)
    elif m1 < m2:
        return 0 #Returning any month before is ok, as year is same!
    
    if d1 > d2:
        return 15*(d1-d2)
    
    return 0
    

# Return Date
d1, m1, y1 = 15, 3, 2024
# Due Date
d2, m2, y2 = 11, 3, 2024

print(libraryFine(d1, m1, y1, d2, m2, y2))