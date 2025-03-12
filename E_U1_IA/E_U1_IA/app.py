import nltk.sem.logic
from nltk.sem.logic import Expression

# Inicializar el analizador
read_expr = Expression.fromstring

# Definir las constantes para Ana, Leon y Angel
ana = read_expr('Ana')
leon = read_expr('Leon')  
angel = read_expr('Angel')  

# Definir los predicados con las constantes
amigos_ana_leon = read_expr('amigos(Ana, Leon)')
amigos_ana_angel = read_expr('amigos(Ana, Angel)')
no_amigos_angel_leon = read_expr('¬amigos(Angel, Leon)')  
trabajan_juntos_ana_angel = read_expr('trabajan(Ana, Angel)')

# Crear un conjunto de fórmulas (separadas por comas)
formulas = [
    amigos_ana_leon,
    amigos_ana_angel,
    no_amigos_angel_leon,
    trabajan_juntos_ana_angel
]

# Imprimir las fórmulas
for formula in formulas:
    print(f"{formula}: {formula}")
