grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Kendrick', 'Aaron'}

grades_calc = [sum(grades[0]) / len(grades[0]),
               sum(grades[1]) / len(grades[1]),
               sum(grades[2]) / len(grades[2]),
               sum(grades[3]) / len(grades[3]),
               sum(grades[4]) / len(grades[4])]

students_average_grades = {'Johnny': grades_calc[0],
                           'Bilbo': grades_calc[1],
                           'Steve': grades_calc[2],
                           'Kendrick': grades_calc[3],
                           'Aaron': grades_calc[4]}

print(students_average_grades)

# Первый способ решения. Изменил в последствии на текущий.

# johnny = sum(grades[0])/len(grades[0])
# bilbo = sum(grades[1])/len(grades[1])
# steve = sum(grades[2])/len(grades[2])
# kendrick = sum(grades[3])/len(grades[3])
# aaron = sum(grades[4])/len(grades[4])
#
# a = {'Johnny:' :johnny,'Bilbo:' : bilbo, 'Steve:' : steve, 'Kendrick:' : kendrick, 'Aaron:' : aaron}
# print(a)
