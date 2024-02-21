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
    st.markdown('<div style="text-align: justify;">Creadores:</p></div>',
        unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.link_button("Liuva Nuñez-Castelo ", "https://www.linkedin.com/in/liuva-nu%C3%B1ez-castelo/")
    col2.link_button("Alex Garea", "https://www.linkedin.com/in/alex-garea-4981a6282/")
    col3.link_button("David Agrazo ", "https://www.linkedin.com/in/davidagrazods/")
    
   

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
