import numpy as np

# Definir una matriz con las distribuciones de probabilidad de (Me gusta, me gusta poco, no me gusta) para 
# cada categoría (fila) y película (columna). Como hay 5 columnas, hay 5 películas/brazos.
PROBABILITY_MATRIX = [
    [(0.5, 0.2, 0.3), (0.2, 0.2, 0.6), (0.3, 0.3, 0.4), (0.4, 0.3, 0.3), (0.1, 0.2, 0.7)], # Hombres mayores de 40 años
    [(0.4, 0.3, 0.3), (0.1, 0.2, 0.7), (0.2, 0.4, 0.4), (0.3, 0.1, 0.6), (0.5, 0.3, 0.2)], # Mujeres mayores de 40 años
    [(0.6, 0.1, 0.3), (0.3, 0.3, 0.4), (0.2, 0.3, 0.5), (0.1, 0.4, 0.5), (0.4, 0.2, 0.4)], # Hombres menores de 40 años
    [(0.3, 0.4, 0.3), (0.2, 0.1, 0.7), (0.5, 0.2, 0.3), (0.4, 0.4, 0.2), (0.3, 0.3, 0.4)]  # Mujeres menores de 40 años
]

def assign_rewards(userDataset): 
    rewards = [] # Recompensas de todos los usuarios

    for user in userDataset:
        user_rewards = [] # Recompensas del usuario
        for probabilities in PROBABILITY_MATRIX[user]:
            reward = np.random.choice([5, 3, 0], 1, p=probabilities)
            user_rewards.append(reward)

        rewards.append(user_rewards)

    return np.array(rewards)