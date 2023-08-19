# instalar y importar las librerias
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.__version__
import seaborn as sns
sns.set()
# Lee el archivo CSV especificando el formato de fecha
aq = pd.read_csv("air_quality_no8.csv", index_col=0, parse_dates=True, dayfirst=True)
# Ver los 5 primeros datos
aq.head()
# Función plot -  imprimir datos de datos
aq.plot()
plt.ylabel("Measurement value")
# plotear una sola estación
aq['station_3'].plot()
