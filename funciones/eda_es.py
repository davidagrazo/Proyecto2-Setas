import streamlit as st
import numpy as np
import pickle
import pandas as pd
import plotly.express as px

def eda_es():
    df= pd.read_csv("funciones/setas.csv")

    with st.expander(label="DataFrame", expanded=False):
        st.dataframe(df)
        
    sombrero = [x for x in df.columns if 'sombrero' in x]

    lamina = [x for x in df.columns if 'lamina' in x]

    tallo = [x for x in df.columns if 'tallo' in x]

    resto = [x for x in df.columns if not any(y in x for y in ('sombrero', 'lamina', 'tallo', 'class') )]

    partes = st.radio("ELIGE UNA CARACTERISTICA", ["SOMBRERO", "LAMINA", "TALLO", "RESTO DE CARACTERISTICAS"], horizontal = True)

    if partes == "SOMBRERO":
        seleccion = st.selectbox(label= "PARTES DEL SOMBRERO", options= sombrero)
  
    if partes == "LAMINA":
        seleccion = st.selectbox(label= "PARTES DE LA LAMINA", options= lamina)
    
    if partes == "TALLO":
        seleccion = st.selectbox(label= "PARTES DEL TALLO", options= tallo)
    
    if partes == "RESTO DE CARACTERISTICAS":
        seleccion = st.selectbox(label= "RESTO DE PARTES", options= resto)

    col1, col2 = st.columns(2)
    
    fig1 = px.bar(data_frame = df,
    x= seleccion, color = "class",barmode='group',
    height=400)
    
    col1.plotly_chart(fig1, use_container_width = True)
    
    fig2 = px.sunburst(data_frame = df,
        path       = [seleccion, 'class'])
    fig2.update_traces(textinfo = "label+percent parent")
    col2.plotly_chart(fig2, use_container_width = True)


    
    
if __name__ == "__main__":
    eda_es()    