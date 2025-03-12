import streamlit as st
import pandas as pd

st.title('🎶 Machine Learning App')

st.info('This is App build a machine learning Model')

df = pd.read_csv('https://github.com/dataprofessor/data/blob/master/penguins_cleaned.csv')
df
