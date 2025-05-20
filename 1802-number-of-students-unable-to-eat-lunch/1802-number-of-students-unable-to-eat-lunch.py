class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        while len(sandwiches) > 0 and len(students) > 0:

            if sandwiches[0] in students:
                if sandwiches[0] == students[0]:
                    students.pop(0)
                    sandwiches.pop(0)
                else:
                    students.append(students.pop(0))   
            else:
                break
        
        return len(students)
        