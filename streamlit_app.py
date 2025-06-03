import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np

st.title("Welcome to ScatterVisualizer for the Wine Dataset")

st.header("Select two Columns and see its scatterplot below!", divider="rainbow")

df = pd.read_csv("wine.csv")

target_map = {1: '1', 2: '2', 3: '3'}
for i in range(len(df)):
    df['Wine'][i] = target_map[df['Wine'][i]]

options = df.columns.tolist()
selection = st.pills("Features:", options, selection_mode="multi")

num_features = len(selection)
color = 'grey'
if num_features <= 2:
    if num_features == 2:
        color = 'green'
    else:
        color = 'grey'
        
    st.badge(f"Your selected options: {selection}.", color=color)
elif num_features > 2:
    st.badge("Too many features! Select two.", color="red")

no_graph_generated = True
st.header("", divider="rainbow")

if num_features == 2:
    no_graph_generated = False
    st.markdown("Your Scatter:")
    st.scatter_chart(df, x=selection[0], y=selection[1], color='Wine')

if no_graph_generated:
    st.markdown("Default Scatter:")
    st.scatter_chart(df, x='Proline', y='Ash', color='Wine')

