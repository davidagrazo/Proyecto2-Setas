import streamlit as st
from streamlit_option_menu import option_menu
from inicio import inicio
from funciones.proyecto2_es import proyecto2es
from funciones.proyecto2_en import proyecto2en

def main():
    st.set_page_config(
        page_title="PROYECTO 2 BOOTCAMP DSB05RT HACKABOSS",
        page_icon=":mushroom:")

    st.title("SEGUNDO PROYECTO -- MACHINE LEARNING")

    liuva = st.link_button("Liuva Nuñez-Castelo ", "https://www.linkedin.com/in/liuva-nu%C3%B1ez-castelo/")
    alex = st.link_button("Alex Garea", "https://www.linkedin.com/in/alex-garea-4981a6282/")
    david = st.link_button("David Agrazo ", "https://www.linkedin.com/in/davidagrazods/")
    
    st.write([liuva, alex, david])

    seleccion = option_menu(
        menu_title=None,
        options=["INFO", "SPANISH VERSION", "ENGLISH VERSION"],
        icons=["info-circle","flag", "flag-fill"],
        default_index=0,
        orientation="horizontal")
    if seleccion == "INFO":
        
        pass

    if seleccion == "SPANISH VERSION":
        proyecto2es()
    
    if seleccion == "ENGLISH VERSION":
        proyecto2en()

if __name__ == "__main__":
    main()
