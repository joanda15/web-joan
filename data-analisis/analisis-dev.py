import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Simulación de los datos de la encuesta (reemplázalos con los datos reales)
data_2 = {
    "Timestamp": ["13/08/2024 21:11:08"],
    "Objective": ["Ofrecer servicios de desarrollo de software."],
    "Audience": ["Todos"],
    "Desired Features": ["Página de inicio con introducción y servicios., Sección de portafolio con proyectos anteriores., Soporte para múltiples idiomas."],
    "Style": ["Moderno y minimalista."],
    "Content": ["Ejemplos de proyectos anteriores."],
    "Devices": ["Dispositivos móviles (smartphones y tablets)."],
    "Security Level": ["Certificado SSL básico."],
    "Update Frequency": ["Según sea necesario."],
    "Budget and Deadline": ["Cuento con cero pesos y tengo plazo de una semana."]
}

df_2 = pd.DataFrame(data_2)
print(df_2.head())

# Conteo de frecuencias para cada columna
objective_counts = df_2['Objective'].value_counts()
audience_counts = df_2['Audience'].value_counts()
features_counts = df_2['Desired Features'].value_counts()
style_counts = df_2['Style'].value_counts()

print("Frecuencia de Objetivo:")
print(objective_counts)

print("\nFrecuencia del Público Objetivo:")
print(audience_counts)

# Gráfico de barras para el objetivo principal
plt.figure(figsize=(10, 6))
sns.barplot(x=objective_counts.values, y=objective_counts.index)
plt.title("Objetivo Principal del Sitio Web")
plt.xlabel("Frecuencia")
plt.ylabel("Objetivo")
plt.show()

# Gráfico de barras para las funcionalidades deseadas
plt.figure(figsize=(10, 6))
sns.barplot(x=features_counts.values, y=features_counts.index)
plt.title("Funcionalidades Deseadas en el Sitio Web")
plt.xlabel("Frecuencia")
plt.ylabel("Funcionalidades")
plt.show()

# Gráfico de calor para combinar funcionalidades y estilo
plt.figure(figsize=(10, 6))
sns.heatmap(df_2[['Desired Features', 'Style']].apply(pd.Series.value_counts).fillna(0), cmap='Blues', annot=True)
plt.title("Combinación de Funcionalidades Deseadas y Estilo Visual")
plt.show()

# Exportar resultados a un archivo CSV
df_2.to_csv('resultados_encuesta_2.csv', index=False)
