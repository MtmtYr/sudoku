# medium
list_sudoku = [
 [2,0,0,0,0,3,7,8,0],
 [0,0,0,9,0,0,1,0,0],
 [7,0,0,0,6,5,0,0,9],
 [0,0,0,0,0,0,0,0,0],
 [5,7,1,0,0,0,3,0,0],
 [0,3,0,0,0,0,8,5,0],
 [0,0,5,0,3,0,0,0,0],
 [6,0,3,0,0,0,0,9,0],
 [9,0,0,1,0,0,0,0,0]]

 list_possible = [i for i in range(1, 10)]

 def narrow_ver(x, list_possible, list_sudoku):
  list_ver = [list_sudoku[i][x] for i in range(9) if type(list_sudoku[i][x]) is int]
  return set(list_possible) - set(list_ver)

 def narrow_hor(y, list_possible, list_sudoku):
  list_hor = [list_sudoku[y][i] for i in range(9) if type(list_sudoku[y][i]) is int]
  return set(list_possible) - set(list_hor)

  def narrow_blo(x, y, list_possible, list_sudoku):
  index_x = (x // 3) * 3
  index_y = (y // 3) * 3
  list_blo = [list_sudoku[i][j] for i in range(index_y, index_y+3) for j in range(index_x, index_x+3) if type(list_sudoku[i][j]) is int]
  return set(list_possible) - set(list_blo)

 def narrow(x, y, list_possible, list_sudoku):
  list_possible = narrow_ver(x, list_possible, list_sudoku)
  list_possible = narrow_hor(y, list_possible, list_sudoku)
  list_possible = narrow_blo(x, y,list_possible, list_sudoku)
  return sorted(list(list_possible))

 def apply_narrow(list_sudoku):
  """
  すべてのセルに対して narrow() を実行する
  """
  for y in range(9):
    for x in range(9):
      if list_sudoku[y][x] != 0 and type(list_sudoku[y][x]) is int:
        continue
      elif list_sudoku[y][x] == 0:
        list_sudoku[y][x] = narrow(x, y, list_possible, list_sudoku)
      else:
        list_sudoku[y][x] = narrow(x, y, list_sudoku[y][x], list_sudoku)
        if len(list_sudoku[y][x]) == 1:
          list_sudoku[y][x] = list_sudoku[y][x][0]
  return list_sudoku
  import copy

 list_possible = [i for i in range(1, 10)]
 count = 0
 temp_sudoku = []
 while(True):
  temp_sudoku = copy.deepcopy(list_sudoku)
  count += 1
  list_sudoku = apply_narrow(list_sudoku)
  if temp_sudoku == list_sudoku:
    break
 print(count)
 list_sudoku


