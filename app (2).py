
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Instrumentos Musicales",
    page_icon="🎵",
    layout="wide"
)

# Título principal
st.title("🎵 Instrumentos Musicales")

st.write(
    "Bienvenido a nuestra página sobre instrumentos musicales. "
    "Aquí podrás conocer diferentes instrumentos, sus familias "
    "y algunas de sus características."
)

# Menú
opcion = st.selectbox(
    "Selecciona una opción:",
    [
        "Inicio",
        "Cuerda",
        "Viento",
        "Percusión",
        "Teclado"
    ]
)

# INICIO
if opcion == "Inicio":

    st.header("🎶 Conoce el mundo de la música")

    st.write(
        "Los instrumentos musicales son objetos creados para producir "
        "sonidos y formar parte de diferentes expresiones musicales."
    )

    st.subheader("🎼 Familias de instrumentos")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("🎸")
        st.write("**Cuerda**")

    with col2:
        st.write("🎺")
        st.write("**Viento**")

    with col3:
        st.write("🥁")
        st.write("**Percusión**")

    with col4:
        st.write("🎹")
        st.write("**Teclado")


# CUERDA
elif opcion == "Cuerda":

    st.header("🎸 Instrumentos de cuerda")

    st.write(
        "Los instrumentos de cuerda producen sonido mediante "
        "la vibración de sus cuerdas."
    )

    st.subheader("Algunos ejemplos")

    st.write("🎸 Guitarra")
    st.write("🎻 Violín")
    st.write("🎼 Arpa")


# VIENTO
elif opcion == "Viento":

    st.header("🎺 Instrumentos de viento")

    st.write(
        "Los instrumentos de viento producen sonido mediante "
        "la vibración del aire."
    )

    st.subheader("Algunos ejemplos")

    st.write("🎺 Trompeta")
    st.write("🎷 Saxofón")
    st.write("🪈 Flauta")


# PERCUSIÓN
elif opcion == "Percusión":

    st.header("🥁 Instrumentos de percusión")

    st.write(
        "Los instrumentos de percusión producen sonido principalmente "
        "cuando son golpeados, sacudidos o frotados."
    )

    st.subheader("Algunos ejemplos")

    st.write("🥁 Batería")
    st.write("🪘 Tambor")
    st.write("🎵 Maracas")


# TECLADO
elif opcion == "Teclado":

    st.header("🎹 Instrumentos de teclado")

    st.write(
        "Los instrumentos de teclado utilizan teclas para producir "
        "diferentes sonidos."
    )

    st.subheader("Algunos ejemplos")

    st.write("🎹 Piano")
    st.write("🎹 Órgano")
    st.write("🎹 Teclado electrónico")
    
