# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - проявите фантазию :)
#import random

class Matrix:
    def __init__(self,  line, column, value=None,):
        self.line = line
        self.column = column
        self.value = value
        self.arr = []
        self.create_Matrix()

    def create_Matrix(self):
        for i in range(self.line):
            self.arr.append([0]*self.column)
        for i in range(self.line):
            for j in range(self.column):
                self.arr[i][j] = self.value

    def print_arr(self):
        for i in self.arr:
            for j in i:
                print(j, end = ' ')
            print()


    def change_symbol(self, symbol, index_line, index_column):
        self.arr[index_line][index_column] = symbol
        self.print_arr()

    def output_line_column(self):
        print(f'Количество строк - {len(self.arr)}, количество колонок - {len(self.arr[-1])}')

    def new_symbol(self, symbol, index_line, index_column):
        add_line = index_line - self.line
        add_column = index_column - self.column
        for item in self.arr:
            for i in range(0, add_column):
                item.append(None)

        self.column = index_column


        for i in range(0, add_line):
            tmp_ar = []
            for j in range(0, self.column):
                tmp_ar.append(None)
            self.arr.append(tmp_ar)


        self.line = index_line
        self.arr = self.arr.copy()
        self.arr[self.line-1][self.column-1] = symbol


        self.print_arr()


x = Matrix(5, 4, 6)

x.output_line_column()

x.change_symbol(0, 2, 1)

x.new_symbol(123, 7, 6)