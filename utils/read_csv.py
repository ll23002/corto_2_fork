import csv
import numpy as np

"""
  Lee un archivo csv y devuelve dos arreglos numpy
  x_values: arreglo de numpy con los valores de x
  y_values: arreglo de numpy con los valores de y
"""
def read_csv(filename):
  x_values = []
  y_values = []
  
  with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)  
    for row in reader:
      if len(row) >= 2:
        try:
          x = float(row[0])
          y = float(row[1])
          x_values.append(x)
          y_values.append(y)
        except ValueError:
          continue
  
  return np.array(x_values), np.array(y_values)