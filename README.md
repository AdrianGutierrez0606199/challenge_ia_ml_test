# challenge_ia_ml_test

## Guía para el Evaluador

Este repositorio contiene la solución al reto de Machine Learning/Análisis de datos para el cargo de Lider de Linea de conocimiento en Bancolombia

### Estructura de Carpetas

- **EDA_parte_1_1/**  
  Análisis exploratorio de datos (EDA) y limpieza inicial.
  - **raw_to_staging/**  
    Scripts y notebooks para limpiar los datos crudos y prepararlos para la zona de staging.
    - `raw_to_staging_cleanup.ipynb`  
      Notebook principal de limpieza y validación de consistencia de los datos crudos.
    - `raw_cleanup.html`  
      Exportación en HTML del notebook anterior para revisión rápida.
  - **staging_to_analytics/**  
    Notebooks para el análisis exploratorio y transformación de los datos desde staging a analytics.
    - `EDA.ipynb`  
      Análisis exploratorio de los datos ya limpios.
    - `EDA_file.html`  
      Exportación en HTML del análisis exploratorio.

- **ML_models_1_2/**  
  Ingeniería de características y entrenamiento de modelos de Machine Learning.
  - `Feature_Engineering_Models.ipynb`  
    Notebook principal con la ingeniería de variables, selección de características y entrenamiento/comparación de modelos (XGBoost, KNN, SVR).
  - `feat_eng_model_selec.html`  
    Exportación en HTML del notebook anterior para revisión rápida.

- **data/**  
  Carpeta para almacenar los datos en sus diferentes estados:
  - **raw/**  
    Datos originales sin procesar.
  - **staging/**  
    Datos limpios y listos para análisis.
  - **analitycs/**  
    Datos finales preprocesados para modelado.

- **input_info/**  
  Información adicional y archivos de apoyo para el reto.

- **nequi_ds_test/**  
  Carpeta independiente con otro test de ciencia de datos (no es parte central del reto principal).

### Archivos Clave

- `README.md`  
  Este archivo, con la guía de navegación y explicación del reto.
- `.gitignore`  
  Configuración para ignorar archivos temporales, binarios y datos pesados.

### ¿Cómo abordar el repositorio?

1. **Comenzar por el EDA:**  
   Revisar la carpeta `EDA_parte_1_1/` para entender el análisis exploratorio y la limpieza de datos. Se recomienda abrir primero los archivos HTML para una revisión rápida, y los notebooks `.ipynb` si se desea ejecutar el código.

2. **Revisar la ingeniería de variables y modelos:**  
   Continuar con la carpeta `ML_models_1_2/`, donde se realiza la ingeniería de características y el entrenamiento de los modelos. El notebook `Feature_Engineering_Models.ipynb` contiene todo el flujo de modelado, desde la selección de variables hasta la comparación de modelos.

3. **Datos:**  
   Los datos procesados no se incluyen por tamaño, pero la estructura de carpetas indica dónde deben ubicarse (`data/raw/`, `data/staging/`, `data/analitycs/`). Si se desea ejecutar los notebooks, colocar los archivos correspondientes en estas rutas.

4. **Exportaciones HTML:**  
   Para una revisión rápida sin necesidad de ejecutar código, se incluyen exportaciones HTML de los notebooks principales.

5. **Notas adicionales:**  
   - Cada notebook contiene comentarios y celdas de texto explicando las decisiones tomadas.
   - El flujo recomendado es: limpieza y EDA → ingeniería de variables → modelado y comparación.
   - Si se requiere reproducibilidad, asegurarse de tener las dependencias de Python indicadas en los notebooks.

---

Cualquier duda sobre la estructura o ejecución, revisar los comentarios dentro de los notebooks o contactar