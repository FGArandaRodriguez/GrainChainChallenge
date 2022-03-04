import copy
import json
import random
import tabulate

class iluminate:

    def __init__(self, matriz):
        self.matriz = copy.deepcopy(matriz)
        self.orden_matriz = copy.deepcopy(matriz)
        self.size_row = 0
        self.size_column = 0
        self.paths = {}
        self.restricciones_matriz()

    #Este metodo validaremos la matríz
    def restricciones_matriz(self):
        self.size_row = len(self.matriz)
        errores = []
        for index, row in enumerate(self.matriz):
            if index == 0:
                self.size_column = len(row)
            if self.size_column != len(row):
                errores.append(f"¡Vaya!, parece que la linea con index {index} solo tiene {len(row)} columnas, debería tener {self.size_column}.")
        if len(errores):
            raise Exception(str(errores))
    
    #Este método nos ayudará a ordenar los focos
    def orden_iluminacion(self):
        return sorted(self.paths, key= lambda i: len(self.paths[i]))
    
    def define_ruta(self):
        def ruta_iluminacion( x, y, indice, mode='top'):
            if x < 0 or y < 0 or x >= self.size_row or \
                y >= self.size_column or self.matriz[x][y]:
                return
            nuevo_indice = f"{x},{y}"

            #validamos qe sean distintos indices
            if indice != nuevo_indice:
                if indice in self.paths.keys():
                    self.paths[indice].append(nuevo_indice)
                else:
                    self.paths.update({indice:[nuevo_indice]})
            #Comenzamos a ordenar los focos
            if mode == 'bottom':
                return ruta_iluminacion(x+1, y, indice, mode)
            elif mode == 'left':
                return ruta_iluminacion(x, y-1, indice, mode)
            elif mode == 'right':
                return ruta_iluminacion(x, y+1, indice, mode)
            return ruta_iluminacion(x-1, y, indice, mode)

        for indiceX, columna in enumerate(self.orden_matriz):
            for indiceY, valor in enumerate(columna):
                indice = f"{indiceX},{indiceY}"
                ruta_iluminacion(indiceX, indiceY, indice)
                ruta_iluminacion(indiceX, indiceY, indice, mode='bottom')
                ruta_iluminacion(indiceX, indiceY, indice, mode='left')
                ruta_iluminacion(indiceX, indiceY, indice, mode='right')

        #Realizamos una copia de este método a modo de secuencia
        seq = copy.deepcopy(self.orden_iluminacion())
        ruta_temporal = []
        #validamos que los key ya existan, si no existen los agregamos, der otra forma los eliminamos
        for key in reversed(seq):
            if key not in ruta_temporal:
                ruta_temporal += self.paths.get(key)
            else:
                del self.paths[key]

    def encender_luz(self,proporcion=0):
        oi = self.orden_iluminacion()
        max_proporciones = len(oi)

        if proporcion > max_proporciones:
            raise Exception(f"Solamente {max_proporciones-1} proporciones, comenzando en 0")
        colores = {}
        matriz = copy.deepcopy(self.orden_matriz)

        def _encender_luz(index, value):
            x,y = index.split(',')
            matriz[int(x)][int(y)] = value
        
        for i, value in enumerate(reversed(oi)):
            if i <= proporcion:
                _encender_luz(value, value)
                colores[value] = "#FFFF00"
                for room in self.paths.get(value):
                    _encender_luz(room, value)
        return matriz, max_proporciones, colores

