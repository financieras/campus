import openpyxl            # importamos la librería openpyxl
from itertools import permutations

# Cuando ya sebemos que queremos trabajar con el archivo campus/pilas/mejor_opcion.xlsm
wb = openpyxl.load_workbook('mejor_opcion.xlsx')
ws4 = wb["Sheet4"]         # accediendo a la hoja4
ws4['E10'] = "Permutaciones"

n = 4
perm = permutations(list(range(1,n+1)))   # obtenemos todas las permutaciones de la lista 

for count, fila in enumerate(list(perm)):             # imprimimos todas las permutaciones
    lista = list(fila)                                # las primera fila es una tupla con (1,2,3,4)
    for j in range(n):
        ws4.cell(row=count+11, column=j+5).value = lista[j]

wb.save('mejor_opcion.xlsx')
wb.close()