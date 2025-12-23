import streamlit as st
from get_data import load_data

df = load_data()

st.header('US-Unfälle Datenanalyse')
st.write(df.head())
