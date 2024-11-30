# Cargar las biblioteca Pandas con el alias 'pd’
# Cargar las biblioteca Matplotlib con el alias ‘plt’
import matplotlib.pyplot as plt
import pandas as pd

# Leer datos del archivo datos.csv
data = pd.read_csv ("datos/datos.csv")

# Vista previa de las primeras 5 líneas de los datos cargados
print(data.head ())


#Graficamos las variables
data.plot(x ='year', y='cost', kind = 'line')
plt.show()

