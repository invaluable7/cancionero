import pandas as pd
uploaded = files.upload()
file_name = list(uploaded.keys())[0]
df = pd.read_excel(file_name)
columnas = df.columns[:3]  # Tomamos las tres primeras columnas (A, B y C)
if len(columnas) < 3:
    print("Error: El archivo no tiene suficientes columnas.")
else:
    col_b, col_c = columnas[1], columnas[2]
busqueda = input("Ingresa el término a buscar: ")
resultados = df[df[col_b].astype(str).str.contains(busqueda, case=False, na=False) |
                df[col_c].astype(str).str.contains(busqueda, case=False, na=False)]
if not resultados.empty:
    print("Resultados encontrados:")
    print(resultados.to_string(index=False))
else:
    print("No se encontraron coincidencias.")
