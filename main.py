import streamlit as st
from streamlit_option_menu import option_menu
from funciones.proyecto2_es import proyecto2es
from funciones.proyecto2_en import proyecto2en

def main():
    st.set_page_config(
        page_title="PROYECTO 2 BOOTCAMP DSB05RT HACKABOSS",
        page_icon=":mushroom:", layout = "wide")

    seleccion = st.sidebar.selectbox(
        label="MENU",
        options=["SPANISH VERSION", "ENGLISH VERSION"])
    
    if seleccion == "SPANISH VERSION":
        proyecto2es()
    
    if seleccion == "ENGLISH VERSION":
        proyecto2en()

    st.sidebar.markdown('<div style="text-align: justify;">CREADORES DEL PROYECTO</p></div>',
        unsafe_allow_html=True)
    st.sidebar.link_button("Liuva Nuñez-Castelo", "https://www.linkedin.com/in/liuva-nu%C3%B1ez-castelo/")
    st.sidebar.link_button("Alex Garea", "https://www.linkedin.com/in/alex-garea-4981a6282/")
    st.sidebar.link_button("David Agrazo", "https://www.linkedin.com/in/davidagrazods/")

    st.sidebar.add_vertical_space(2)
    st.sidebar.link_button("REPO IN KAGGLE", "https://www.kaggle.com/code/davidagrazo/proyecto-2-setas")
    
if __name__ == "__main__":
    main()
