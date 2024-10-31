# %%
# Carregando a biblioteca numpy
import numpy as np

# %%
# Criando um array de uma dimensão que armazena arrays que armazenam valores inteiros, cada array, representa um usuário e cada coluna um filme.
ratings = np.array(
    [
        [5, 3, 4, 4, np.nan, 1, 2, 1, 3, 3], # user 1
        [3, 1, 2, 3, 3, 4, 3, 4, 3, 5], # user 2
        [4, 2, 3, 4, 4, 3, 5, 2, 1, 1], # user 3
        [0, 5, 5, 2, 1, 4, 2, 5, 5, 5], # user 4
        [2, 4, 2, 1, 2, 2, 1, 3, 4, 4]  # user 5
    ]
)

# %%
# Verificando a forma do array
ratings.shape

# %%
print(ratings)

# %%
# Removendo valores nan e substituindo pela média da avaliação do usuário
for i in range(ratings.shape[0]):
    for j in range(ratings.shape[1]):
        if np.isnan(ratings[i, j]):
            ratings[i, j] = round(np.nanmean(ratings[i]))

# %%
print(ratings)

# %%
# Criando um array com o tamanho da coluna do array ratings e preenchdo com 0s
col_means = np.zeros(ratings.shape[1])

# %%
# Calculando a Média dos filmes por usuário
for i in range(ratings.shape[1]):
    for j in range(ratings.shape[0]):
        if ratings[j, i] != 0:
            col_means[i] += ratings[j, i]

# %%
print(f"Média da avaliação dos filmes: {col_means / ratings.shape[0]}")

# %%
