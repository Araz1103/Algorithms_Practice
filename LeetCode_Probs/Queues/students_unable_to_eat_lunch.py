"""
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

 

Example 1:

Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0 
Explanation:
- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.
Example 2:

Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Output: 3
 

Constraints:

1 <= students.length, sandwiches.length <= 100
students.length == sandwiches.length
sandwiches[i] is 0 or 1.
students[i] is 0 or 1.
"""
from collections import defaultdict, Counter

# def countStudents(students, sandwiches):
#     """
#     :type students: List[int]
#     :type sandwiches: List[int]
#     :rtype: int
#     """
#     # The breaking cases will be that 
#     # 1. Students has all 1s and sandwich on top of stack is 0
#     # 2. Students have all 0s and sandwiches on top of stack is 1
#     # 3. Both lists are empty

#     student_counter = dict(Counter(students))

#     student_all_1s = student_counter.get(1, 0) !=0 and student_counter.get(0, 0) == 0
#     student_all_0s = student_counter.get(0, 0) !=0 and student_counter.get(1, 0) == 0

#     total_num_students = len(students)
#     students_unable_to_eat = total_num_students
#     # Basically keep a current student pointer and a current sandwich pointer
#     # For the student queue, we need a head and tail pointer
#     # When incrementing student pointer, check ->
#     #   If pointer exceeds tail, it starts again from head
#     # If sandwich not compatible, increment student pointer
#     # If sandwich compatible
#     # - increment sandwich pointer
#     # - increment head pointer
#     head_pointer = 0
#     tail_pointer = total_num_students - 1
#     current_student_pointer = 0
#     current_sandwich_pointer = 0
#     top_sandwich_0 = sandwiches[current_sandwich_pointer]==0
#     top_sandwich_1 = sandwiches[current_sandwich_pointer]==1
#     while not ((student_all_1s and top_sandwich_0) or (student_all_0s and top_sandwich_1)):
        
#         print("Student", student_counter)

#         # Check current student can eat current sandwich or not
#         student_type = students[current_student_pointer]
#         sandwich_type = sandwiches[current_sandwich_pointer]

#         print("Current Student", student_type)
#         print("Current Sandwich", sandwich_type)

#         print("Current Student P", current_student_pointer)
#         print("Current Sandwich P", current_sandwich_pointer)

#         if current_sandwich_pointer == 3:
#             break
        
        
#         if student_type==sandwich_type:
#             # Subtract from Counters
#             student_counter[student_type] -=1

#             # Decrement students unable to eat
#             students_unable_to_eat -=1

#             # If students unable to eat is 0, then break
#             if students_unable_to_eat == 0:
#                 return 0 #Fast Break

#             #Increment Pointers

#             # Sandwich Pointer
#             current_sandwich_pointer +=1

#             # Student Pointer (Head shifts)
#             head_pointer += 1

#             if current_student_pointer==tail_pointer:
#                 current_student_pointer = head_pointer
#             else:
#                 current_student_pointer +=1

#         else:
#             # Just incrementing student counter
#             if current_student_pointer==tail_pointer:
#                 current_student_pointer = head_pointer
#             else:
#                 current_student_pointer +=1

#         # Updating values
#         student_all_1s = student_counter.get(1, 0) !=0 and student_counter.get(0, 0) == 0
#         student_all_0s = student_counter.get(0, 0) !=0 and student_counter.get(1, 0) == 0

#         top_sandwich_0 = sandwiches[current_sandwich_pointer]==0
#         top_sandwich_1 = sandwiches[current_sandwich_pointer]==1

#     # If breaks out of the condition, then no more students can eat

#     return students_unable_to_eat

# Simpler Approach
# The order of the sandwiches matter
# If @top of the stack, we have no student who can eat, we return num students
# Else, eventually, one student will eat that sandwich
# So we just loop through the sandwich and decrement until no students are willing to eat

def countStudents(students, sandwiches):
    """
    :type students: List[int]
    :type sandwiches: List[int]
    :rtype: int
    """

    student_counter = Counter(students) #Creates a Hashmap of counts
    initial_count = len(students)

    # Above takes O(n)

    for sw in sandwiches: #O(n)
        if student_counter[sw] > 0:
            initial_count -=1
            student_counter[sw] -=1
        else: # No student willing to eat
            return initial_count

    # Total Time Complexity is O(n)
    # Space needed for Hashmap is O(1)
    # As only 2 types of keys

    return initial_count


print(countStudents([1, 1, 1, 1], [0, 1, 1, 1]))
print("------------")
print(countStudents([1, 0, 1, 1], [0, 0, 0, 0]))
print("-------------")
print(countStudents([1,1,0,0], [0,1,0,1]))
        