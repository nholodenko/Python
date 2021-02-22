class Matrix:
 def __init__(self, matrix):
  self.matrix = matrix

 def __str__(self):
  for i in self.matrix:
   print(*i, sep=' ')
  return ''

 def __add__(self, other):
  for i in range(len(self.matrix)):
   for j in range(len(other.matrix[i])):
    self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
  return Matrix.__str__(self)


m1 = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
m2 = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2], [2, 2, -7]])
print(m1 + m2)







