import numpy as np
import csv
import os

def generate_csv(fx, x_range, num_points=100, filename="data.csv"):
    """
    Genera un archivo CSV con valores x aleatorios y sus correspondientes valores y=F(x).
    
    Parámetros:
    -----------
    fx : función
        Una función que toma un array de numpy como entrada y devuelve valores y
    x_range : tupla
        Una tupla (min_x, max_x) que define el rango de valores x
    num_points : int, opcional
        Número de puntos a generar (predeterminado: 100)
    filename : str, opcional
        Nombre del archivo CSV a crear (predeterminado: "data.csv")
    
    Retorna:
    --------
    str
        Ruta al archivo CSV generado
    """
    # Desempaquetar el rango
    min_x, max_x = x_range
    
    # Generar valores x aleatorios dentro del rango (no distribuidos uniformemente)
    x_values = min_x + (max_x - min_x) * np.random.random(num_points)
    
    # Calcular valores y usando la función proporcionada
    y_values = fx(x_values)
    
    # Redondear valores x e y a 4 decimales
    x_values = np.round(x_values, 4)
    y_values = np.round(y_values, 4)
    
    # Combinar valores x e y en pares
    data_points = list(zip(x_values, y_values))
    
    # Escribir los datos en un archivo CSV
    csv_path = os.path.join(os.getcwd(), filename)
    with open(csv_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['x', 'y'])  # Encabezado
        csv_writer.writerows(data_points)
    
    return csv_path
