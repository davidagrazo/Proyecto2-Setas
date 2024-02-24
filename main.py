import streamlit as st
from streamlit_option_menu import option_menu
from inicio import inicio
from funciones.proyecto2_es import proyecto2es
from funciones.proyecto2_en import proyecto2en

def main():
    st.set_page_config(
        page_title="PROYECTO 2 BOOTCAMP DSB05RT HACKABOSS",
        page_icon=":mushroom:")

    st.sidebar(label= "CREADORES")
    
    st.sidebar.page_link("https://www.linkedin.com/in/liuva-nu%C3%B1ez-castelo/", label="Liuva Nuñez-Castelo ")
    st.sidebar.page_link("https://www.linkedin.com/in/alex-garea-4981a6282/", label="Alex Garea")
    st.sidebar.page_link("https://www.linkedin.com/in/davidagrazods/", label="David Agrazo")
    
   

    seleccion = st.sidebar.selectbox(
        label="Menu",
        options=["INFO", "SPANISH VERSION", "ENGLISH VERSION"])

    if seleccion == "INFO":
        inicio()     
        
    if seleccion == "SPANISH VERSION":
        proyecto2es()
    
    if seleccion == "ENGLISH VERSION":
        proyecto2en()

if __name__ == "__main__":
    main()
