[Probar_en]:https://replit.com/@AnthonyO6/PersonalClassicPoints#main.py



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

# import readchar
# import replit
# import random

# def createMap(path):
#   """
#   This saves the map as a string vector:
  
#   open file reader
#   read file into content
#   close file reader
#   turn the contents into single characters
#   remove the new line characrters '\n'
#   remove the white spaces left behind 
#   """
#   with open(path, 'r') as file:
#     contents = file.read()  
#   # f = open(path)
#   # contents = f.read()
#   # f.close()
#   # https://www.pythonpool.com/python-remove-newline-from-list/ (used to remove \n)
# # https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings (used to remove white spaces)
#   res = [x for x in list(map(lambda x:x.strip(),list(contents))) if x]
#   return res

# def createMatrix(rowCount, colCount, dataList):   
#     """
#     This turns the string map to a matrix
#     """
#     mat = []
#     for i in range(rowCount):
#         rowList = []
#         for j in range(colCount):
#             if dataList[j] not in mat:          #https://stackoverflow.com/questions/40120892/creating-a-matrix-in-python-without-numpy
#               rowList.append(dataList[rowCount * i + j])
#         mat.append(rowList)
#     return mat 

# def matrixMap():
#   """
#   This registers the string map and then 
#   turns it into a matrix
#   From here we can update the matrix before 
#   printing it
#   """
#   alpha = createMap(path = "mydata" + str(random.randint(1,4)) + ".txt")
#   mat = createMatrix(21,21,alpha) 
#   return(mat)


# def movements():
#   """
#   This will:
#   Save matrix map to mat 2 
#   Then save the location of ther person into p_location
#   Then update P location into matrix first at (0,0)
#   and then with "." and then with 'P' in
#   one direction relative to the key press 
#   """
#   # Iniciar en P en (0,0)
#   p_location = list([0,0])
#   mat2 = matrixMap()
#   mat2[0][0] = 'P'
#   # test = None

#   while True:
#     kp = readchar.readkey()
    
#     if kp == 'D' and mat2[p_location[0]][p_location[1]+1] != '#':
#       replit.clear()
#       mat2[p_location[0]][p_location[1]] = '.'
#       mat2[p_location[0]][p_location[1]+1] = 'P' 
#       p_location[1] += 1  
#     elif kp == 'S' and mat2[p_location[0]+1][p_location[1]] != '#':
#       replit.clear()
#       mat2[p_location[0]][p_location[1]] = '.'
#       mat2[p_location[0]+1][p_location[1]] = 'P'   
#       p_location[0] += 1  
#     elif kp == 'A' and mat2[p_location[0]][p_location[1]-1] != '#':
#       replit.clear()
#       mat2[p_location[0]][p_location[1]] = '.'
#       mat2[p_location[0]][p_location[1]-1] = 'P' 
#       p_location[1] -= 1  
#     elif kp == 'W' and mat2[p_location[0]-1][p_location[1]] != '#':
#       replit.clear()
#       mat2[p_location[0]][p_location[1]] = '.'
#       mat2[p_location[0]-1][p_location[1]] = 'P'
#       p_location[0] -= 1  
#     elif kp == 'Q':
#       return kp
#     elif kp == 'D' and mat2[p_location[0]][p_location[1]+1] == '#':
#       replit.clear()
#       pass
#     elif kp == 'S' and mat2[p_location[0]+1][p_location[1]] == '#':
#       replit.clear()
#       pass
#     elif kp == 'A' and mat2[p_location[0]][p_location[1]-1] == '#':
#       replit.clear()
#       pass
#     elif kp == 'W' and mat2[p_location[0]-1][p_location[1]] == '#':
#       replit.clear()
#       pass
#     # testing index error boundries not solved as yet
#     # elif p_location in [1,0]:
#     #   #global test
#     #   test = 'D'
#     #   #continue

#     for line in mat2:
#       mapst =  '  '.join(map(str, line)) 
#       print(mapst)   
#       # print(p_location)
#       # print(test)

# def main(): 
#   # print map once 
#   mat3 = matrixMap()
#   mat3[0][0] = 'P'
#   for line in mat3:
#     mapst =  '  '.join(map(str, line))
#     print(mapst)
    
#   # print movement on map
#   movements()

# if __name__ == "__main__":
#     main()


# Proyecto integrador 5------------------------------------------


# Implementa la clase Juego, ahora el mapa y las posiciones inicial y final son atributos de esta clase, reescribe todas tus funciones anteriores de forma que sean métodos de la clase y todo esté encapsulado.

import readchar
import replit
import random
from dataclasses import dataclass, field



# ahorita como esta la clase funciona pero no es un juego
# seria instanciar diferentes instancias de la misma clase
# problema con el path 
# path is an attribute de la clase no de la instancia 
# hacer mi propio init para casa dinstancia 



@dataclass
class Juego:
  p_location: list = field(default_factory=lambda: [0,0])
  rowCount: int = 21
  colCount: int = 21
  
  def path():
    path = "mydata" + str(random.randint(1,4)) + ".txt"
    return path
    
  with open(path(), 'r') as file:
    contents = file.read()   
  res = [x for x in list(map(lambda x:x.strip(),list(contents))) if x]

  def createMatrix(self):   
      mat = []
      for i in range(self.rowCount):
          rowList = []
          for j in range(self.colCount):
              if self.res[j] not in mat:         
                rowList.append(self.res[self.rowCount * i + j])
          mat.append(rowList)
      return mat
  
  def movements(self):
    mat2 = self.createMatrix()
    mat2[0][0] = 'P'

    while True:
      kp = readchar.readkey()
      
      if kp == 'D' and mat2[self.p_location[0]][self.p_location[1]+1] != '#':
        replit.clear()
        mat2[self.p_location[0]][self.p_location[1]] = '.'
        mat2[self.p_location[0]][self.p_location[1]+1] = 'P' 
        self.p_location[1] += 1  
      elif kp == 'S' and mat2[self.p_location[0]+1][self.p_location[1]] != '#':
        replit.clear()
        mat2[self.p_location[0]][self.p_location[1]] = '.'
        mat2[self.p_location[0]+1][self.p_location[1]] = 'P'   
        self.p_location[0] += 1  
      elif kp == 'A' and mat2[self.p_location[0]][self.p_location[1]-1] != '#':
        replit.clear()
        mat2[self.p_location[0]][self.p_location[1]] = '.'
        mat2[self.p_location[0]][self.p_location[1]-1] = 'P' 
        self.p_location[1] -= 1  
      elif kp == 'W' and mat2[self.p_location[0]-1][self.p_location[1]] != '#':
        replit.clear()
        mat2[self.p_location[0]][self.p_location[1]] = '.'
        mat2[self.p_location[0]-1][self.p_location[1]] = 'P'
        self.p_location[0] -= 1  
      elif kp == 'Q':
        return kp
      elif kp == 'D' and mat2[self.p_location[0]][self.p_location[1]+1] == '#':
        replit.clear()
        pass
      elif kp == 'S' and mat2[self.p_location[0]+1][self.p_location[1]] == '#':
        replit.clear()
        pass
      elif kp == 'A' and mat2[self.p_location[0]][self.p_location[1]-1] == '#':
        replit.clear()
        pass
      elif kp == 'W' and mat2[self.p_location[0]-1][self.p_location[1]] == '#':
        replit.clear()
        pass
  
      for line in mat2:
        mapst =  '  '.join(map(str, line)) 
        print(mapst)   

  def main(self): 
    mat3 = self.createMatrix()
    mat3[0][0] = 'P'
    
    for line in mat3:
      mapst =  '  '.join(map(str, line))
      print(mapst)

    self.movements()
  
if __name__ == "__main__":
  juego = Juego()
  print(juego.main())
