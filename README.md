# 📊 Prueba Técnica – Motor de Predicción de Ventas  
**Licorera "El Buen Gusto"**

Este proyecto implementa un sistema de análisis y predicción de ventas utilizando Python y herramientas de código abierto, con el objetivo de ayudar a la empresa a optimizar inventario, mejorar su gestión comercial y aumentar sus ingresos. La solución está estructurada en tres fases: análisis exploratorio, modelado predictivo y recomendaciones de negocio. Cada fase se entrega en un Jupyter Notebook independiente (.ipynb), acompañado por un reporte ejecutivo dirigido a la gerencia.

---

## 📁 Estructura del Proyecto

```
prueba-tecnica-el-buen-gusto/
│
├── data/                     # Contiene 'ventas_licorera.csv' generado por script
├── notebooks/                # Notebooks para análisis y modelos
│   ├── analisis_exploratorio.ipynb
│   └── modelado_predictivo.ipynb
├── scripts/                  # Script generador de datos
│   └── script_generar_dataset.py
├── reporte/                  # Reporte ejecutivo en PDF
│   └── reporte_ejecutivo.pdf
├── requirements.txt          # Dependencias del proyecto
├── .gitignore
└── README.md
```

---

## 📦 Librerías / Paquetes Utilizados

| Paquete     | Versión   | Descripción                                     |
|-------------|-----------|-------------------------------------------------|
| pandas      | 2.2.3     | Manipulación de datos tabulares                |
| numpy       | 2.2.4     | Cálculos numéricos                             |
| matplotlib  | 3.8.3     | Gráficos y visualizaciones 2D                  |
| seaborn     | 0.13.2    | Gráficos estadísticos avanzados                |
| plotly      | 5.15.0    | Visualización interactiva y gráfica avanzada   |
| scikit-learn| 1.2.2     | Modelos de machine learning                    |
| xgboost     | 1.7.5     | Algoritmo de boosting para regresión y clasificación|
| lightgb     | 3.3.5     | Algoritmo de boosting eficiente y rápido       |
| statsmodels | 0.14.0    | Modelos estadísticos y análisis de series temporales|
| prophet     | 1.1.2     | Modelado de series temporales con forecasting  |
| joblib      | 1.2.0     |Serialización y almacenamiento de objetos       |
| jupyter     | 1.1.1     | Ejecución de notebooks interactivos            |
| ipykernel   | 6.29.5    | Kernel para ejecutar Python dentro de Jupyter  |

Instalación rápida:
```bash
pip install pandas numpy matplotlib seaborn plotly scikit-learn xgboost lightgbm statsmodels prophet joblib jupyter ipykernel

```

---

## ⚙️ Instrucciones de Instalación y Ejecución

### 🧾 Generar el archivo CSV

1. Abre la terminal y navega a la carpeta de scripts:
```bash
cd "C:\Users\kenit\Downloads\Prueba tecnica\scripts"
```

2. Ejecuta el script:
```bash
python script_generar_dataset.py
```
Esto generará el archivo `ventas_licorera.csv` en la carpeta `data/`.

Asegúrate de que el script use la ruta correcta:
```python
filename = '../data/ventas_licorera.csv'
```

---

### 🚀 Opción Rápida: Usar Kernel de Python Global

1. Desde la raíz del proyecto, instala dependencias:
```bash
pip install pandas numpy matplotlib seaborn plotly scikit-learn xgboost lightgbm statsmodels prophet joblib jupyter ipykernel

```

2. O bien, usa el archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

3. Abre el archivo:
```
notebooks/analisis_exploratorio.ipynb
```

4. Verifica que el kernel activo sea Python 3 (global).

5. Ejecuta con:
- `Shift + Enter`: ejecuta celda actual
- `Ejecutar todo`: desde el menú de Jupyter o VS Code

---

### 💻 Opción con Jupyter Notebook (desde navegador)

1. Instala las dependencias:
```bash
pip install pandas numpy matplotlib seaborn plotly scikit-learn xgboost lightgbm statsmodels prophet joblib jupyter ipykernel
```

2. Ejecuta Jupyter:
```bash
jupyter notebook
```

3. Se abrirá en el navegador con la dirección http://localhost:8888/tree. Navega a:
```
notebooks/analisis_exploratorio.ipynb
```

4. Verifica que el kernel diga: `Python 3 (ipykernel)`

5. Ejecuta celdas:
- `Shift + Enter`: celda actual
- `Ejecutar todo`: menú superior

---

### ✅ Opción Recomendable: Entorno Virtual

1. Crear entorno virtual:
```bash
python -m venv venv_buengusto
```

2. Activar entorno (en PowerShell):
```bash
.\venv_buengusto\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. En VS Code:
   - `Ctrl + Shift + P`
   - Selecciona: `Python: Select Interpreter`
   - Elige: `venv_buengusto/Scripts/python.exe`

5. Abre y ejecuta el notebook normalmente:
```
notebooks/analisis_exploratorio.ipynb
```

6. Ejecuta celdas:
- `Shift + Enter`: ejecutar una celda
- `Ctrl + Enter`: ejecutar sin avanzar

---

## 🧠 Resumen del Enfoque

Este proyecto resuelve el desafío de predecir ventas en una cadena de licorerías mediante análisis exploratorio, modelos de predicción y recomendaciones accionables. Se exploran las tendencias de venta por categoría, estacionalidad, promociones, eventos especiales, zonas geográficas y variables climáticas. Se identifican patrones que permiten anticipar la demanda y tomar decisiones más informadas.

La solución utiliza Python y librerías de código abierto en Jupyter Notebooks para mantener claridad y trazabilidad. El enfoque busca ser explicable para perfiles no técnicos, utilizando visualizaciones claras, conclusiones orientadas al negocio y modelos seleccionados según métricas como MAE, RMSE y MAPE. Todo esto se integra en un reporte ejecutivo conciso para la toma de decisiones.

---



