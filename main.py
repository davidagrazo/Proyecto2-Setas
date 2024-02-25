import streamlit as st
from streamlit_option_menu import option_menu
from inicio import inicio
from funciones.proyecto2_es import proyecto2es
from funciones.proyecto2_en import proyecto2en

def main():
    st.set_page_config(
        page_title="PROYECTO 2 BOOTCAMP DSB05RT HACKABOSS",
        page_icon=":mushroom:")

    seleccion = st.sidebar.selectbox(
        label="MENU",
        options=["INICIO", "SPANISH VERSION", "ENGLISH VERSION"])
    if seleccion == "INICIO":
        inicio()

    if seleccion == "SPANISH VERSION":
        proyecto2es()
    
    if seleccion == "ENGLISH VERSION":
        proyecto2en()

    st.sidebar.link_button("Liuva Nuñez-Castelo", "https://www.linkedin.com/in/liuva-nu%C3%B1ez-castelo/")
    st.sidebar.link_button("Alex Garea", "https://www.linkedin.com/in/alex-garea-4981a6282/")
    st.sidebar.link_button("David Agrazo", "https://www.linkedin.com/in/davidagrazods/")
    
if __name__ == "__main__":
    main()
