# %%
import numpy as np

# %%
ratings = np.array(
    [
        [5, 3, 4, 4, np.nan, 1, 2, 1, 3, 3], # user 1
        [3, 1, 2, 3, 3, 4, 3, 4, 3, 5], # user 2
        [4, 2, 3, 4, 4, 3, 5, 2, 1, 1], # user 3
        [1, 5, 5, 2, 1, 4, 2, 5, 5, 5], # user 4
        [2, 4, 2, 1, 2, 2, 1, 3, 4, 4]  # user 5
    ]
)

# %%
ratings.shape

# %%
print(ratings)

# %% Tratamento
for i in range(ratings.shape[0]):
    for j in range(ratings.shape[1]):
        if np.isnan(ratings[i, j]):
            ratings[i, j] = round(np.nanmean(ratings[i]))

# %%
print(ratings)

# %%