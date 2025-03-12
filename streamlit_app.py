import streamlit as st
import pandas as pd

st.title('🎶 Machine Learning App')

st.info('This is App build a machine learning Model')

with st.expander('Data') :
  st.write ('***Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df
 
  st.write ('***x**')
  x = df.drop('species', axis = 1)
  x

  st.write ('***y**')
  y = df.species
  y
