#  В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки
# заносятся в таблицу. Каждой группе отведена своя строка. Определите группу с
# наилучшим средним баллом.

from random import randint as RI

def create_grades():
    groups = 5
    grades = [0] * groups
    for i in range(groups):
        grades[i] = list(RI(2,5) for s in range(RI(20,30)))
    return grades

def find_max_average(grades):
    average_grades = []

    for grades_in_group in grades:
        average = 0
        for grade in grades_in_group:
            average += grade
        average_grades.append(round(average/len(grades_in_group), 2))
        
    for grades_in_group in grades:
        print(grades_in_group)

    print(average_grades)

    max_grade = max(average_grades)
    number_group = average_grades.index(max_grade)
    print(f'Highest average grade is - {max_grade}. Number of group is - {number_group + 1}')

find_max_average(create_grades())

# Дана квадратная матрица, заполненная случайными числами. Определите,
# сумма элементов каких строк превосходит сумму главной диагонали матрицы.

size = 4
matrix = [0] * size

for i in range(size):
    matrix[i] = list(RI(1,10) for c in range(size))
for i in matrix:
    print(i)

sum_diagonal = 0
for i in range(size):
    print(matrix[i][i], end = ' ')
    sum_diagonal += matrix[i][i]
print()
print(sum_diagonal)

sum_in_rows = []
for i in matrix:
    sum_in_rows.append(sum(i))
print(sum_in_rows)

for i in range(len( sum_in_rows)):
    if sum_in_rows[i] > sum_diagonal:
        print(f'In {i+1} group sum is higher, then sum of element in diagonal')


#  В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. 
#  Каждому месяцу соответствует своя строка. 
#  Определите самый жаркий и самый холодный 7-дневный промежуток этого периода.


size = 4
period = 7
matrix = [0] * size

for i in range(size):
    matrix[i] = list(RI(1,10) for c in range(size))

for i in matrix:
    print(i)

matrix_in_row = []

for row_matrix in matrix:
    for el in row_matrix:
        matrix_in_row.append(el)

print(matrix_in_row)

average_temp = []

for i in range(len(matrix_in_row) - period + 1):
    average_temp.append(sum(matrix_in_row[i:i+period]))

print(average_temp)

max_el = max(average_temp)
index_max_el = average_temp.index(max_el)
print(max_el)
print(index_max_el)

start_x = 0
start_y = 0
for index_x in range(len(matrix)):
    if len(matrix[index_x]) > index_max_el:
        print(f'max element in stroke {matrix[index_x]} is {matrix[index_x][index_max_el]}')
        start_x = index_x
        start_y = index_max_el
        break
    else:
        index_max_el -= len(row_matrix)

for i in range(period):
    index_y = start_y + i
    lenght = len(matrix[start_x])
    start_x = start_x + (start_y + i)//len(matrix[start_x])
    index_y = (start_y + i)%len(matrix[start_x])
    print(matrix[start_x][index_y], end =' ')


