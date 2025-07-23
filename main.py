import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('netflix_titles.csv')

# Mostrar las primeras 5 filas del dataset
print("\nPrimeras 5 filas del dataset:")
print(df.head())

# Mostrar información básica del dataset
print("\nInformación del dataset:")
print(df.info())
