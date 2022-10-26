class Solution(object):
    def countStudents(self, students, sandwiches):
        
        while (len(sandwiches) > 0) and (len(students) > 0):

            boolean = sandwiches[0] in students

            if boolean == False:
                break

            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))


        return(len(students))
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        