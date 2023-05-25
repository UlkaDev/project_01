# Задача 4.1.
# Домашнее задание на SQL
import columns as columns
# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:


import pandas as pd
import sqlite3

connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = 'CREATE TABLE IF NOT EXISTS Students (Student_Id INTEGER, Student_name TEXT, School_Id INTEGER PRIMARY KEY);'
cursor.execute(query)
connection.commit()

data = [[201, 'Иван', 1], [202, 'Петр', 2], [203, 'Анастасия', 3], [204, 'Игорь', 4]]
df = pd.DataFrame(data, columns=['Student_Id', 'Student_name', 'School_Id'])
df.to_sql('Students', connection, if_exists='replace', index= False)


def get_inf(Student_id):
    connection = sqlite3.connect('teatchers.db')
    cursor = connection.cursor()
    query2 = 'SELECT Students.Student_Id, Students.Student_name, Students.School_Id, School.School_name FROM Students, School WHERE Students.School_Id = School.School_Id and Student_Id = ?'
    cursor.execute(query2, (Student_id,))
    for i in cursor.fetchall():
        print(f'ID Студента: {Student_id} \n'
              f'Имя студента: {i[1]} \n'
              f'ID школы: {i[2]} \n'
              f'Название школы: {i[3]}')
    connection.close()

get_inf(input('Введите ID студента '))
