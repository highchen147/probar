import pandas as pd
import numpy as np

print("Hola mundo")

x = np.arange(0,100,2)

# Este es un comentario de prueba
with open("nuevo3.txt", "w") as file:
    for i in x:
        print(i, file=file)

# Este es otro comentario de prueba 