import pandas as pd
from sklearn.datasets import load_wine

wine_dataset = load_wine()
wine_df = pd.DataFrame(wine_dataset.data, columns=wine_dataset.feature_names)

print(wine_df.info())
print(wine_df.count())
print(wine_df.mean())
print(wine_df.std())
# print(wine_df.std())
print(wine_df.describe())

