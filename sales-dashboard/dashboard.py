import streamlit as st
import pandas as pd
import pickle
import plotly.express as px

# ────────────────────────────────────────────────────────────────
# 1) Configuración de la página
st.set_page_config(
    page_title="Sales Forecast Demo",
    layout="wide",
)
st.title("🛍️ Sales Forecast Demo")
st.write("Carga tu dataset preprocesado y obtén las predicciones en el backend.")
# ────────────────────────────────────────────────────────────────

# 2) Carga del modelo serializado
with open("linreg_model.pkl", "rb") as f:
    model = pickle.load(f)

# 3) Sidebar: uploader de CSV
st.sidebar.header("Carga de datos")
uploaded_file = st.sidebar.file_uploader(
    "📂 Sube tu validation_set.csv",
    type=["csv"]
)

if uploaded_file:
    # 4.1) Leer el CSV completo
    df_raw = pd.read_csv(uploaded_file)

    # 4.2) Mostrar vista previa de lo cargado
    st.subheader("Datos cargados (raw)")
    st.dataframe(df_raw.head(5), use_container_width=True)

    # 4.3) Preparar matriz de features para el modelo
    feature_cols = list(model.feature_names_in_)
    X_new = df_raw.reindex(columns=feature_cols, fill_value=0)

    # 4.4) Ejecutar la predicción en el backend
    preds = model.predict(X_new)

    # 4.5) Construir DataFrame de salida con Category, season y prediction
    df_out = pd.DataFrame({
        "Category":   df_raw["Category"],
        "season":     df_raw["season"],
        "prediction": preds
    })
    # 4.6) Ordenar de mayor a menor
    df_out = df_out.sort_values("prediction", ascending=False).reset_index(drop=True)

    # 4.7) Mostrar tabla de resultados
    st.subheader("🔝 Predicción por categoría y temporada")
    st.dataframe(df_out, use_container_width=True)

    # ────────────────────────────────────────────────────────────
    # 5) Dos pie charts: primavera (season 1) y verano (season 2)
    st.subheader("📊 Distribución por categoría en cada temporada")
    col1, col2 = st.columns(2)

    # Filtrar para primavera (1)
    df_spring = df_out[df_out["season"] == 1]
    fig_spring = px.pie(
        df_spring,
        names="Category",
        values="prediction",
        title="Primavera (season 1)"
    )
    col1.plotly_chart(fig_spring, use_container_width=True)

    # Filtrar para verano (2)
    df_summer = df_out[df_out["season"] == 2]
    fig_summer = px.pie(
        df_summer,
        names="Category",
        values="prediction",
        title="Verano (season 2)"
    )
    col2.plotly_chart(fig_summer, use_container_width=True)
    # ────────────────────────────────────────────────────────────

    # 6) Descargar el CSV con predicciones ordenadas
    csv_download = df_out.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Descargar predicciones ordenadas",
        data=csv_download,
        file_name="predicciones_ordenadas.csv",
        mime="text/csv"
    )

else:
    st.info("🔍 Empieza subiendo tu validation_set.csv para ver las predicciones.")

# ────────────────────────────────────────────────────────────────
# 7) Notas finales
st.markdown("""
---
**Cómo funciona**  
1. El usuario sube un CSV con las columnas dummy (`Category_*`, `season_*`).  
2. El backend reindexa para crear cualquier columna faltante con 0 y llama a `model.predict()`.  
3. Se muestra `Category`, `season` y `prediction` ordenadas.  
4. Dos pie charts muestran la participación de cada categoría en primavera y verano.  
5. El usuario puede descargar el resultado en CSV.
""")
