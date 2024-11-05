# Clasificación de Niveles de Riesgo en la Calidad del Aire: Un Estudio Comparativo entre SVM y Random Forest
Este proyecto desarrolla y compara dos modelos de aprendizaje automático, SVM (Support Vector Machines) y Random Forest, para clasificar los niveles de riesgo en la calidad del aire basados en concentraciones de diversos contaminantes. Los resultados buscan apoyar el diseño de sistemas de alerta en tiempo real para la protección de la salud pública.

## Objetivos del Proyecto
1. Implementar un sistema de clasificación que asigne niveles de riesgo de calidad del aire: Bajo, Moderado o Alto.
2. Comparar la precisión, eficiencia y aplicabilidad de SVM y Random Forest en la clasificación de niveles de riesgo.
3. Seleccionar el modelo óptimo para un sistema de alertas, evaluando la interpretación y capacidad de respuesta en tiempo real.

## Datos

Los datos utilizados en este proyecto se obtuvieron de: [UCI Air Quality Dataset en Kaggle](https://www.kaggle.com/datasets/dakshbhalala/uci-air-quality-dataset?resource=download). Este conjunto de datos incluye mediciones de calidad del aire, recolectadas en varios intervalos de tiempo.

### Características Clave del Conjunto de Datos

- **Fecha y Hora:** Fecha y hora de la medición.
- **Concentraciones de Contaminantes:** Incluyen CO, NMHC, NOx, y NO2.
- **Mediciones de Sensores:** Niveles reportados por varios sensores de calidad del aire.

Este conjunto de datos es adecuado para tareas de clasificación y permite realizar análisis predictivo y de series temporales en el contexto de la calidad del aire.