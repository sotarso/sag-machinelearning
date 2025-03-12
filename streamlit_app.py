import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


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

with st.expander('Data visualization'):
   st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')
 
