import streamlit as st
from streamlit_option_menu import option_menu
from funciones.proyecto2_es import proyecto2es
from funciones.proyecto2_en import proyecto2en

def main():
    st.set_page_config(
        page_title="PROYECTO 2 BOOTCAMP DSB05RT HACKABOSS",
        page_icon=":mushroom:")

    seleccion = st.sidebar.selectbox(
        label="Menu",
        options=["SPANISH VERSION:es:", "ENGLISH VERSION :uk:"])

    if seleccion == "SPANISH VERSION:es:":
        proyecto2es()
    
    if seleccion == "ENGLISH VERSION :uk:":
        proyecto2en()

    st.sidebar.link_button("Liuva Nuñez-Castelo :flag-gb:", "https://www.linkedin.com/in/liuva-nu%C3%B1ez-castelo/")
    st.sidebar.page_link("https://www.linkedin.com/in/alex-garea-4981a6282/", label="Alex Garea")
    st.sidebar.page_link("https://www.linkedin.com/in/davidagrazods/", label="David Agrazo")
    
if __name__ == "__main__":
    main()
