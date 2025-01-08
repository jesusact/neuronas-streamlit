import streamlit as st

st.image("img_neurona.jpg", width=360)

st.title("¡Hola neurona!")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Res entradas y sesgo"])

with tab1:
    st.header("Una neurona con una entrada y un peso")
    peso = st.slider(
        "Peso",
        min_value=0.0,
        max_value=5.0,
        value=1.0, 
    )
    number = float(st.number_input("Introduzca el valor de la entrada", value=0.0))
    st.button("Calcular la salida", "button1")
    if st.button:
        st.write(f"La salida de la neurona es {number * peso}")


with tab2:
    col1, col2 = st.columns(2)

    with col1:
       st.write("Peso w0")
       w0 = st.slider("s1", 0.0, 5.0, label_visibility="collapsed")
       st.write("Entrada x0")
       x0 = st.number_input("input1", label_visibility="collapsed")

    with col2:
       st.write("Peso w1")
       w1 = st.slider("s2", 0.0, 5.0, label_visibility="collapsed")
       st.write("Entrada x1")
       x1 = st.number_input("input2", label_visibility="collapsed")
    
    if st.button("Calcular la salida", "button2"):
        st.text(f"La salida de la neurona es {x0 * w0 + x1 * w1}")


with tab3:
    col1, col2, col3 = st.columns(3)

    with col1:
       st.write("Peso w0")
       w0 = st.slider("s3", 0.0, 5.0, label_visibility="collapsed")
       st.write("Entrada x0")
       x0 = st.number_input("input3", label_visibility="collapsed")

    with col2:
       st.write("Peso w1")
       w1 = st.slider("s4", 0.0, 5.0, label_visibility="collapsed")
       st.write("Entrada x1")
       x1 = st.number_input("input4", label_visibility="collapsed")

    with col3:
       st.write("Peso w2")
       w2 = st.slider("s5", 0.0, 5.0, label_visibility="collapsed")
       st.write("Entrada x2")
       x2 = st.number_input("input5", label_visibility="collapsed")
   
    b = st.number_input("Introduzca el valor del sesgo")
        
    if st.button("Calcular la salida", "button3"):
        st.text(f"La salida de la neurona es {x0 * w0 + x1 * w1 + x2 * w2 + b}")
