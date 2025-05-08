# Sales Forecast Demo

**English (Español al final)**

## 🚀 Main Problem

* Companies struggle to anticipate which product categories will sell best in upcoming seasons, leading to overstock, missed opportunities, and lost revenue.

## 🛠️ What We Built

A lightweight Streamlit app that:

1. Loads a preprocessed CSV of historical sales grouped by category and season.
2. Applies a serialized Linear Regression model in the backend.
3. Predicts demand per category for spring and summer.
4. Visualizes top predictions and distribution via interactive tables and pie charts.

## ⚡ Quick Start

1. Clone this repo:

   ```bash
   git clone https://github.com/Hacanaval/The-Stock-Stack.git
   cd The-Stock-Stack/sales-dashboard
   ```
2. Create and activate your virtual environment, then install dependencies:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run the app:

   ```bash
   streamlit run dashboard.py
   ```
4. Upload `validation_set.csv` in the sidebar to see predictions.

## 📂 Repo Structure

* `The-Stock-Stack.ipynb` — Full notebook with preprocessing & model training.
* `sales-dashboard/` — Streamlit demo folder:

  * `dashboard.py` — Main app script.
  * `linreg_model.pkl` — Serialized regression model.
  * `validation_set.csv` — Preprocessed features for demo upload.
  * `requirements.txt` — Python dependencies.

## 📝 Steps We Followed

1. Cleaned and prepared raw sales data in Pandas.
2. Grouped by category & season, computed average demand.
3. One-hot encoded features; trained a Linear Regression model.
4. Serialized model with Pickle.
5. Built a Streamlit interface for easy predictions and visuals.

## 🔮 Future Improvements

* Upgrade to advanced models (RandomForest, XGBoost, Prophet).
* Automate CSV preprocessing within the app.
* Deploy on Streamlit Cloud or Heroku for public access.

---

## Español

## 🚀 Problema Principal

* Las empresas tienen dificultades para anticipar qué categorías de productos se venderán mejor en las próximas temporadas, provocando exceso de inventario, oportunidades perdidas y pérdida de ingresos.

## 🛠️ Qué Construimos

Una app ligera en Streamlit que:

1. Carga un CSV preprocesado de ventas históricas agrupadas por categoría y temporada.
2. Aplica un modelo de Regresión Lineal serializado en el backend.
3. Predice la demanda por categoría para primavera y verano.
4. Visualiza las predicciones principales y la distribución mediante tablas interactivas y gráficos de torta.

## ⚡ Inicio Rápido

1. Clona este repositorio:

   ```bash
   git clone https://github.com/Hacanaval/The-Stock-Stack.git
   cd The-Stock-Stack/sales-dashboard
   ```
2. Crea y activa tu entorno virtual, luego instala dependencias:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Ejecuta la app:

   ```bash
   streamlit run dashboard.py
   ```
4. Sube `validation_set.csv` en la barra lateral para ver las predicciones.

## 📂 Estructura del Repo

* `The-Stock-Stack.ipynb` — Notebook con preprocesamiento y entrenamiento.
* `sales-dashboard/` — Demo en Streamlit:

  * `dashboard.py` — Script principal.
  * `linreg_model.pkl` — Modelo serializado.
  * `validation_set.csv` — Features preprocesadas para el demo.
  * `requirements.txt` — Dependencias de Python.

## 📝 Pasos Realizados

1. Limpieza y preparación de datos en Pandas.
2. Agrupación por categoría y temporada, cálculo de demanda.
3. One-hot encoding de features; entrenamiento de Regresión Lineal.
4. Serialización del modelo con Pickle.
5. Construcción de la interfaz con Streamlit para predicciones y visualizaciones.

## 🔮 Mejoras Futuras

* Mejorar modelos (RandomForest, XGBoost, Prophet).
* Automatizar el preprocesamiento dentro de la app.
* Desplegar en Streamlit Cloud o Heroku para acceso público.
