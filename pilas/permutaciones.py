from itertools import permutations


perm = permutations([1,2,3,4])   # todas las permutaciones de la lista 

for i in list(perm):             # imprimimos todas las permutaciones
    print (list(i))                   # con el asterisco se muestran las tuplas sin paréntesis ni comas
