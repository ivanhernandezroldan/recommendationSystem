import numpy as np
import random

# Definir los conjuntos de datos --> conjunto de usuarios organizado por subconjuntos/categorias:
    # Subconjuntos:
    #[0] --> Hombres mayores de 40 años
    #[1] --> Mujeres mayores de 40 años
    #[2] --> Hombres menores de 40 años
    #[3] --> Mujeres menores de 40 años
DATASET1 = np.array([0] * 2500 + [1] * 1250 + [2] * 750 + [3] * 500) #Almacena 2500 '0's, 1250 '1's, ...
DATASET2 = np.array([0] * 1500 + [1] * 1250 + [2] * 1250 + [3] * 1000)

# Crear una lista con las constantes
datasets = [DATASET1, DATASET2]

def getRandomDataset (): 
    dataset = random.choice(datasets) # Seleccionar un dataset aleatorio
    np.random.shuffle(dataset) 
    return dataset