import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Simulación de los datos de las encuestas (puedes reemplazar esto con tus datos reales)
data = {
    "Timestamp": ["13/08/2024 21:08:55", "13/08/2024 21:14:03"],
    "Purpose": ["Explorar el portafolio de proyectos.", "Contratar servicios de desarrollo de software."],
    "Content": ["Recursos gratuitos (tutoriales, guías, etc.).", "Descripción detallada de servicios ofrecidos."],
    "Navigation": ["Seguridad al navegar.", "Facilidad de uso y navegación intuitiva."],
    "Services": ["Análisis de datos y visualización.", "Desarrollo web completo."],
    "Contact": ["Chat en vivo.", "Llamada telefónica."],
    "Features": ["Chat en vivo para consultas rápidas.", "Calculadora de presupuesto en línea."],
    "Security": ["Muy importante.", "Muy importante."]
}

df = pd.DataFrame(data)
print(df.head())

# Conteo de frecuencias para cada columna
purpose_counts = df['Purpose'].value_counts()
content_counts = df['Content'].value_counts()
navigation_counts = df['Navigation'].value_counts()
services_counts = df['Services'].value_counts()

print("Frecuencia de Propósitos:")
print(purpose_counts)

print("\nFrecuencia de Contenido:")
print(content_counts)

# Gráfico de barras para el propósito de la visita
plt.figure(figsize=(10, 6))
sns.barplot(x=purpose_counts.values, y=purpose_counts.index)
plt.title("Propósito de Visita al Sitio Web")
plt.xlabel("Frecuencia")
plt.ylabel("Propósito")
plt.show()

# Gráfico de barras para el contenido de interés
plt.figure(figsize=(10, 6))
sns.barplot(x=content_counts.values, y=content_counts.index)
plt.title("Contenido de Interés en el Sitio Web")
plt.xlabel("Frecuencia")
plt.ylabel("Contenido")
plt.show()

# Combinación de contenido y servicios en un gráfico
plt.figure(figsize=(10, 6))
sns.heatmap(df[['Content', 'Services']].apply(pd.Series.value_counts).fillna(0), cmap='Blues', annot=True)
plt.title("Combinación de Contenido y Servicios")
plt.show()

# Exportar resultados a un archivo CSV
df.to_csv('resultados_encuestas.csv', index=False)

