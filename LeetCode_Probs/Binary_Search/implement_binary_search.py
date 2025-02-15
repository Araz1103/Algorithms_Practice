
def binary_search(arr, k):
    l_p = 0
    r_p = len(arr) - 1

    while l_p <= r_p:
        m_p = (l_p + r_p)//2

        if k==arr[m_p]:
            return m_p
        
        if k < arr[m_p]:
            r_p = m_p - 1

        else:
            l_p = m_p + 1
    
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 7, 8], 7))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 7, 8], 0))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 7, 8], 2))
print(binary_search(["a", "b", "b", "c", "c", "d", "e", "e", "f"], "c"))
print(binary_search(["a", "b", "b", "c", "c", "d", "e", "e", "f"], "z"))


