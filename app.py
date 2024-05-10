# app.py
#    streamlit
# by: Astrid, Diba, Julius

# imports
import streamlit as st
import pandas as pd


# constants
feats = ["aadt_koret", "aadt_cykle", "vejnavn", "taelle_dat", "geometry"]
df = pd.read_csv("data/trafiktaelling.csv")
plots_folder = "plots"

# content
st.set_page_config(page_title="Trafic",layout="wide")
st.title("How trafic spreads throughout Copenhagen")
st.write("There are many famous measures, most notably is probably mean, median, variance, and standard deviation. However, these measures fall short of describing phenomena like: _how_ does a given variable spread over a given shape/geography. Similar to the relationship between mean and median, there are various ways to answer this. We will focus on what is perhaps the simplest: Moran's I, to answer the question, how does bikes spread throughout the city. At one extreme, we would have bikes exclusively placed in a certain area, at another extreme, we would have bikes spread out in small pockets. Understanding how this varies throughout the city of Copenhagen can help inform city planning decisions, explain why certain areas are better to bike in, hint at what spaces are most shared between people, and more. Moran's I thus becomes intersting for both the hypothetical city planner and, more importantly, the biking citizenry of Copenhagen.")
st.table(df.head())
cols = st.columns(2)
cols[0].image("plots/0.jpg")
cols[1].write("There are many famous measures, most nota")
st.image("plots/0.jpg")
st.write("balallaglalalbalallaglalalbalallaglalalbalallaglalalbalallaglalalbalallaglalalba balallaglalallallaglalal")
variable = st.sidebar.text_input("hi")
st.write(df[variable])

# st.bokeh_plot(bokeh_plot)