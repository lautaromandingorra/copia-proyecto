import streamlit as st
import matplotlib.pyplot as plt

def pregunta1(res):  #res seria la lista de respuestas a las preguntas
    tab1, tab2, tab3 = st.tabs(["¿En qué ciudades se hicieron más mediciones?", "Pregunta siguiente", "Pregunta siguiente"])


    with tab1:
        st.header("Gráfica de mediciones")
        data = res[0]                                                               #toma el elemento 0 de la lista res,osea toma el valor de libreria(en este caso seria la libreria que da el main de la funcion mas apariciones)
        names = list(data.keys())                                                   #hace una lista con el nombre de cada key de libreria, osea de cada ciudad
        values = list(data.values())                                                #hace una lista con el valor de cada value de libreria, osea de cada aparicion
        fig, ax = plt.subplots(figsize=(20, 16))
        ax.bar(names, values)
        ax.tick_params(axis = "x",labelcolor='black', rotation= 270, labelsize=20 ) # rota los nombres hacia abajo y agranda la letra de los valores en x
        ax.tick_params(axis = "y", labelsize=20 , labelcolor='black'  )             #cambia el tamaño de los valores en y #agrege labelcolor='black', solo para tener en cuenta el cambio de color
        maximo = max(values)                                                        # da el valor maximo de values
        y_lista = list(range(0, maximo + 40, 40))                                   # genera una lista de valores desde 0 hasta el maximo mas 30
        y_lista.append(maximo)                                                      # a la lista y_lista le agrega el valor del maximo
        ax.set_yticks(y_lista)                                                      #los valores que se muestran en y 
        #plt.tight_layout()                                                          # evita que se corten
        st.pyplot(fig)



    with tab2:
        st.header("Representación")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=1080)
    with tab3:
        st.header("Representacion")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=1080)