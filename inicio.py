import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

def inicio():
    st.markdown("## INTRODUCCION")
    
    
    add_vertical_space(1)

    st.markdown(
        '<div style="text-align: justify;">Nuestro Segundo Proyecto corresponde a nuestra entrada en el mundo de MACHINE LEARNING, de utilizar modelos de regresión o de clasificación, si necesitamos reducir dimensionalidad para lograr un mejor modelo,...</p></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify;">Para esta ocasión nos decidimos a usar un dataset de Setas de la UCI Machine Learning Repository</p></div>', unsafe_allow_html=True)

    add_vertical_space(1)

    st.markdown(
        '<div style="text-align: justify;">Analizamos las partes que componen una seta y pasamos a realizar el EDA para revisar la estructura de los datos</p></div>', unsafe_allow_html=True)

    st.page_link("https://archive.ics.uci.edu/dataset/73/mushroom", label="DATASET UCI", icon="🏫")
    



if __name__ == "__main__":
    inicio()