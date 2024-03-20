import pandas as pd
import os

# Obtener la lista de archivos CSV en el directorio actual
def merge_data(input_dir, output_dir):
    csv_files = [file for file in os.listdir(input_dir) if file.endswith('.csv')]

    # Leer cada archivo CSV y combinarlos en un solo DataFrame
    all_data = pd.DataFrame()
    for file in csv_files:
        df = pd.read_csv(os.path.join(input_dir, file))
        all_data = pd.concat([all_data, df])

    # Guardar el DataFrame combinado en un nuevo archivo CSV
    all_data.to_csv(os.path.join(output_dir, 'sales.csv'), index=False)
    
def check_and_merge_data(directory):
    # Verificar si hay archivos CSV en el directorio
    csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
    if not csv_files:
        # Si no hay archivos CSV, llamar a la función merge_data
        merge_data(directory)
    else:
        print("Ya existen archivos CSV en el directorio. No se necesita fusionar.")