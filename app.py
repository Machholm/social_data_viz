# app.py
#    streamlit
# by: Astrid, Julius

# imports
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

with open("plots/aadt_koret_map.html", 'r') as f:
    car_string = f.read()
    
with open("plots/aadt_cykle_map.html", 'r') as f:
    bike_string = f.read()
    
with open("plots/bokeh.html", 'r') as f:
    bokeh_string = f.read()
    
# constants
feats = ["aadt_koret", "aadt_cykle", "vejnavn", "taelle_dat", "geometry"]
df = pd.read_csv("data/trafiktaelling.csv")
plots_folder = "plots"

# content
st.set_page_config(page_title="Traffic in Copenhagen")  #,layout="wide")
st.title("How trafic spreads throughout Copenhagen")
st.caption("By Astrid Machholm and Julius Olander")

# introduction
st.write("Copenhagen is the city over half a million people call home, while over 62 million overnight stays are spent by tourists from around the world each year[1]. Citizens commuting to and from work and tourists exploring the city’s many blooming cultural and gastronomic locations present great logistical mobility challenges with regard to city infrastructure. As in many other cities, Copenhagen commuting is done by walking on foot, driving by car, and taking public transport such as buses and trains. But what makes Copenhagen truly special is its municipality’s massive efforts towards becoming “the world’s best bicycling city” as part of its strategy to become more carbon neutral, and reduce noise pollution and traffic bottlenecks, while furthering public health. On an average day, over 1.4 million kilometers are traveled by bike collectively, and the city houses over 745.000 bikes and more than 380 kilometers of bike lanes [2].")
st.write("In this article, we look at some of the publicly available data from the Copenhagen Municipality regarding traffic counts throughout the city. Through analysis of the data, we dive into tendencies in commuting to provide a basis for exploration that can support future decision-making and investments. The data spans 2009 to 2023 and includes manually counted observations of different transportation forms. The main focus is on the two primary forms of transportation, but it is also possible to explore other transportation forms used in the city, including pedestrians, electric scooters, buses, and more.")

# line chart
st.image("plots/plot_dual.png", caption="test test test")

# Moran's I map

#cols = st.columns(2)
#cols[0].
#cols[1].
#cols[1].write("There are many famous measures, most nota")
components.html(bike_string,height=600)
components.html(car_string,height=600)

st.html(car_string)

st.html(bike_string)

st.image("plots/morans_bikes.png")
st.image("plots/morans_cars.png")

# Moran's I tiles

# bar chart
components.html(bokeh_string,height=600)



#st.table(df.head())
#cols = st.columns(2)
#cols[0].image("plots/0.jpg")
#cols[1].write("There are many famous measures, most nota")
#st.image("plots/0.jpg")
#st.write("balallaglalalbalallaglalalbalallaglalalbalallaglalalbalallaglalalbalallaglalalba balallaglalallallaglalal")
#variable = st.sidebar.text_input("hi")
#st.write(df[variable])

# st.bokeh_plot(bokeh_plot)