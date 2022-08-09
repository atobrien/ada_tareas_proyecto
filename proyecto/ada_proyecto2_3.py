

# Proyecto integrador 2------------------------------------------

# Instrucciones: Escribir un programa que corra un bucle infinito leyendo e 
# imprimiento las teclas y sólo terminará cuando se presione la tecla ↑ 
# indicada como 

# !pip install readchar
# import readchar

# while True:
#   keypress = readchar.readkey()
#   if keypress == readchar.key.UP:
#     break
#   else:
#     print(keypress)


# Proyecto integrador 3------------------------------------------

# Iniciar con un número en 0, leer la tecla `n` del teclado en un bucle, por cada presionada, borrar la terminal y e imprimir el nuevo número hasta el número 50.

# import readchar
# import replit

# i = 0
# while True:
#   keypress = readchar.readkey()
#   if keypress == 'n':
#     i += 1
#     replit.clear()
#     if i == 51:
#       break
#     for k in range(-1+i,i):
#       print(k)
#       continue
    
# Proyecto integrador 4------------------------------------------
    
# Implementar una función que reciba el mapa de un laberinto en forma de cadena, y lo convierta a matriz de caracteres.

import readchar
import replit
  
def createMap(path):
  """
  This saves the map as a string vector:
  
  open file reader
  read file into content
  close file reader
  turn the contents into single characters
  remove the new line characrters '\n'
  remove the white spaces left behind 
  """
  f = open(path)
  contents = f.read()
  f.close()
  # https://www.pythonpool.com/python-remove-newline-from-list/ (used to remove \n)
# https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings (used to remove white spaces)
  res = [x for x in list(map(lambda x:x.strip(),list(contents))) if x]
  return res

def createMatrix(rowCount, colCount, dataList):   
    """
    This turns the string map to a matrix
    """
    mat = []
    for i in range(rowCount):
        rowList = []
        for j in range(colCount):
            if dataList[j] not in mat:          #https://stackoverflow.com/questions/40120892/creating-a-matrix-in-python-without-numpy
              rowList.append(dataList[rowCount * i + j])
        mat.append(rowList)
    return mat 

def matrixMap():
  """
  This registers the string map and then 
  turns it into a matrix
  From here we can update the matrix before 
  printing it
  """
  alpha = createMap(path = "mydata.txt")
  mat = createMatrix(21,21,alpha) 
  # mat[0][0] = 'P'
  # mat[20][19] = '0'
  return(mat)

def personLocation():
  """
  This saves the current person location
  in a list 
  """
  p_location = []
  for n in range(len(matrixMap())):
    for i in range(len(matrixMap()[0])):
      if mat2()[n][i] == 'P':
        p_location = list([n,i])
        for p in range(1):
          p_location[p]
  return(p_location)

# def endLocation():
#   """
#   This saves the ending location
#   in a list 
#   """
#   end_location = [20,20]
#   return end_location

def movements():
  """
  This will:
  Save matrix map to mat 2 
  Then save the location of ther person into p_location
  Then update P location into matrix first at (0,0)
  and then with "." and then with 'P' in
  one direction relative to the key press 
  """
  #while True:
    # keypress = readchar.readkey()
  mat2 = matrixMap()

  p_location = []
  # This is storing the location of P
  for n in range(len(mat2)):
    for i in range(len(mat2[0])):
      if mat2[n][i] == 'P':
        p_location = list([n,i])
  print(p_location)
    # if p_location == []:
    #     mat2[0][0] = 'P'
    #     print(p_location)        
            

    # for kp in keypress:
    #   if kp == 'A' and mat2[p_location[0]][p_location[1]+1] != '#':
    #     replit.clear()
    #     mat2[p_location[0]][p_location[1]] = '.'
    #     mat2[p_location[0]][p_location[1]+1] = 'P' 
    #     return mat2
    #     pass
    #   elif kp == 'W' and mat2[p_location[0]+1][p_location[1]] != '#':
    #     replit.clear()
    #     mat2[p_location[0]][p_location[1]] = '.'
    #     mat2[p_location[0]+1][p_location[1]] = 'P'   
    #     return mat2
    #     pass 
    #   elif kp == 'D' and mat2[p_location[0]][p_location[1]-1] != '#':
    #     replit.clear()
    #     mat2[p_location[0]][p_location[1]] = '.'
    #     mat2[p_location[0]][p_location[1]-1] = 'P' 
    #     return mat2
    #     pass
    #   elif kp == 'S' and mat2[p_location[0]-1][p_location[1]] != '#':
    #     replit.clear()
    #     mat2[p_location[0]][p_location[1]] = '.'
    #     mat2[p_location[0]-1][p_location[1]] = 'P'
    #     return mat2
    #     pass 
    #   elif kp == 'E':
    #     break

    

  
def matrixMapToStringMap():
  """
  This prints the map matrix to a string matrix
  for easy viewing
  """
  for line in movements():
    mapst =  '  '.join(map(str, line))
    # why when i use return it gives single line 
    print(mapst)
  
def main():  
  movements()
  # while True:
  #   matrixMapToStringMap()
  

if __name__ == "__main__":
    main()



  
