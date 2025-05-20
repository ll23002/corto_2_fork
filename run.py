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
  # -------------------- INSERTE IMPLEMENTACION AQUI ------------------#

  n = len(x_values)
  # Si hay menos de 4 puntos, no podemos hacer interpolación cúbica
  if n < 4:
    return np.array([]), np.array([])

  h = np.diff(x_values) #h[k] = x_values[k+1] - x_values[k]

  a = y_values  # a_k = y_k

  # 3. Configurar el sistema de ecuaciones para encontrar los c_k
  SystemMatrix = np.zeros((n, n))#Matriz con ceros de tamaño n x n, no confundir con la matriz aumentada Ax=b
  RHS_vector = np.zeros(n)#solucion de matriz

  # Condiciones de frontera naturales: c_0 = 0 y c_{n-1} = 0
  SystemMatrix[0, 0] = 1
  RHS_vector[0] = 0

  SystemMatrix[n - 1, n - 1] = 1
  RHS_vector[n - 1] = 0

  # Valores de cada fila de la matriz
  for k in range(1, n - 1):
    # Coeficientes de la matriz (tridiagonal)
    SystemMatrix[k, k - 1] = h[k - 1]
    SystemMatrix[k, k] = 2 * (h[k - 1] + h[k])
    SystemMatrix[k, k + 1] = h[k]

    # Lado derecho del vector
    RHS_vector[k] = 3 * ((a[k + 1] - a[k]) / h[k] - (a[k] - a[k - 1]) / h[k - 1])

  #resuelve la matriz de la forma SystemMatrix * c = RHS_vector
  c = np.linalg.solve(SystemMatrix, RHS_vector)

 #Inicializar los vectores b y d con ceros
  b = np.zeros(n - 1)
  d = np.zeros(n - 1)

  for k in range(n - 1):
    # Fórmula para b_k
    b[k] = (a[k + 1] - a[k]) / h[k] - (h[k] / 3) * (2 * c[k] + c[k + 1])

    # Fórmula para d_k
    d[k] = (c[k + 1] - c[k]) / (3 * h[k])

  # 6. Evaluar los polinomios para los nuevos valores de x (new_x)
  new_x = np.linspace(0, 100, 50)
  new_y = np.zeros_like(new_x)  # Inicializamos el array para los nuevos valores de y con ceros

  #Devuelve la posicion de cada new_x si estuviera en x_values, el -1 es porque necesitamos el valor inicial del intervalo
  indices = np.searchsorted(x_values, new_x) - 1

  indices[indices < 0] = 0  # Asegura que los puntos antes de x_0 usen el primer intervalo
  indices[indices >= n - 1] = n - 2  # Asegura que los puntos después de x_{n-1} usen el último intervalo

  # Evaluar el polinomio P_i(x) = a_i + b_i(x-x_i) + c_i(x-x_i)^2 + d_i(x-x_i)^3
  for j, x_eval in enumerate(new_x):
    i = indices[j]  # El índice del intervalo [x_i, x_{i+1}] para este x_eval
    #valor actual x - valor inicial x del intervalo
    delta_x = x_eval - x_values[i]

    # Evaluar P_i(x_eval)
    new_y[j] = a[i] + b[i] * delta_x + c[i] * delta_x ** 2 + d[i] * delta_x ** 3
    #exportar a excel

  i = 0
  for x, y in zip(new_x, new_y):
    i += 1
    print(f"{i}: ({x}, {y})")

  return new_x, new_y


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