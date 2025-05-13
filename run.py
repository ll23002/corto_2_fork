import numpy as np
from utils.read_csv import read_csv
from utils.canvas import Canvas
from utils.generate_csv import generate_csv
"""
  Implementa la funcion de Interpolacion de lagrange paga generar un nuevo dataset
  a partir de los valores de x e y leidos del archivo csv
  x_values: arreglo de numpy con los valores de x
  y_values: arreglo de numpy con los valores de y
  new_x: arreglo de numpy con los nuevos valores de x
  new_y: arreglo de numpy con los nuevos valores de y

  deberas generar un nuevo data set con valores de x en un intervalo el 0 - 100, 
  generando 50 puntos espaciados regularmente

  luego de implementar y retornar dichos valores, corre run.py para verificar que 
  la grafica se genere correctamente

"""
def generate_dataset(x_values, y_values):
  #-------------------- INSERTE IMPLEMENTACION AQUI ------------------#


  return [], [] # nuevo dataset, con valores de x e y
  #-------------------- INSERTE IMPLEMENTACION AQUI ------------------#


def main():

  # Generar un archivo CSV con valores aleatorios
  generate_csv(lambda x: x**3 + 4*x**2 + 3, (0, 100), num_points=50, filename="data.csv")

  x_values, y_values = read_csv("data.csv")

  new_x, new_y = generate_dataset(x_values, y_values)
  canvas = Canvas(title="My Plot", xlabel="X-axis", ylabel="Y-axis")
  canvas.add_dataset(x_values, y_values, label="valores del csv", color="blue")
  canvas.add_dataset(new_x, new_y, label="valores generados de interpolacion", color="red")

  canvas.show()

if __name__ == "__main__":
  main()