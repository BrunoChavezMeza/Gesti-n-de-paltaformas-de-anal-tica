#Creamos el archivo de la APP en el interprete principal (Phyton)

#############################IMPLEMENTACIÓN DE DASHBOARD################################

#Importamos librerias
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from funpymodeling.exploratory import freq_tbl 

#################################################################

#Definimos la instancia de streamlit
@st.cache_resource

#################################################################

#Creamos la función de carga de datos
def load_data():
    #Lectura del archivo csv sin indice
    df1=pd.read_csv("titanic.csv")
    #Carga desde un archivo csv con indice
    df2= pd.read_csv("titanic.csv", index_col= 'Name')
    
#################################################################

    #Etapa de procesamiento de Datos
   
    #ANÁLISIS UNIVARIADO DE FRECUENCIAS
    #Obtengo un análisis univariado de una variable categórica en específico
    table= freq_tbl(df1['Sex'])
    #Obtengo un filtro de los valores más reelevantes de la variables categórica seleccionada
    Filtro= table[table['frequency']>1]
    #Ajusto el indice de mi dataframe
    Filtro_index1= Filtro.set_index('Sex')        
    
    #Selecciono las columnas tipo numericas del dataframe Filtro_index1
    numeric_df1 = Filtro_index1.select_dtypes(['float','int'])  #Devuelve Columnas
    numeric_cols1= numeric_df1.columns                          #Devuelve lista de Columnas 

    #Selecciono las columnas tipo numericas del dataframe df2
    numeric_df2 = df2.select_dtypes(['float','int'])  #Devuelve Columnas
    numeric_cols2= numeric_df2.columns                #Devuelve lista de Columnas    
      

    return Filtro_index1, df2, numeric_df1, numeric_cols1, numeric_df2, numeric_cols2 

#Cargamos los datos obtenidos de la funcion "load_"
Filtro_index1,df2,numeric_df1,numeric_cols1,numeric_df2,numeric_cols2 = load_data()

#########################Creación del dashboard#################################

#1. CREACIÓN DE LA SIDEBAR
#Generamos los encabezados para la barra lateral (sidebar)
st.sidebar.title("DASHBOARD")
st.sidebar.header("Sidebar")
st.sidebar.subheader("Panel de selección")

#2 CREACIÓN DE LOS FRAMES
#Generamos los Frames que utilizaremos en el diseño
#Widget 1:Selectbox
#Menu desplegable de opciones de los frames seleccionados
Frames= st.selectbox(label="Frames",options=["Frame 1","Frame 2","Frame 3","Frame 4"])

#################################################################

#3. CONTENIDO DEL FRAME 1
if Frames == "Frame 1":
    #Generamos los encabezados para el dashboard
    st.title("TITANIC")
    st.header("Frame Principal")
    st.subheader("Line Plot")
    
    #Widget 2: Checkbox
    #Generamos un cuadro de selección (Checkbox) en una barra lateral (sidebar) para mostrar dataset
    check_box = st.sidebar.checkbox(label= "Mostrar Dataset")
    #Condicional para que aparezca el dataframe
    if check_box:
        #Mostramos el dataset
        st.write(Filtro_index1)
        st.write(df2)
        
    #Widget 3: Multiselect box
    #Generamos un cuadro de multi-selección (Y) para seleccionar variables a graficar
    Vars_num_selected= st.sidebar.multiselect(label="Variables graficadas", options= numeric_cols2)
      
    #GRAPH 1: LINEPLOT
    #Despliegue de un line plot, definiendo las variables "X categorias" y "Y numéricas" 
    figure1 = px.line(data_frame=df2, x=df2.index, 
                  y= Vars_num_selected, title= str('Features of Passengers by name'), 
                  width=1600, height=600)
    #Mostramos el lineplot
    st.plotly_chart(figure1)

