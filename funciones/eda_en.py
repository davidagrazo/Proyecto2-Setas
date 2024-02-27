import streamlit as st
import numpy as np
import pickle
import pandas as pd
import plotly.express as px

def eda_en():
    df= pd.read_csv("funciones/mushrooms_eda.csv")

    with st.expander(label="DataFrame", expanded=False):
        st.dataframe(df)
        
    cap = [x for x in df.columns if 'CAP' in x]

    gill = [x for x in df.columns if 'GILL' in x]

    stalk = [x for x in df.columns if 'STALK' in x]

    other = [x for x in df.columns if not any(y in x for y in ('CAP', 'GILL', 'STALK', 'CLASS'))]

    partes = st.radio("CHOOSE AN OPTION", ["CAP", "GILL", "STALK", "OTHERS"], horizontal = True)

    if partes == "CAP":
        seleccion = st.selectbox(label= "CAP'S PARTS", options= cap)
  
    if partes == "GILL":
        seleccion = st.selectbox(label= "GILL'S PARTS", options= gill)
    
    if partes == "STALK":
        seleccion = st.selectbox(label= "STALK'S PARTS", options= stalk)
    
    if partes == "OTHERS":
        seleccion = st.selectbox(label= "OTHERS", options= other)

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
    eda_en()    