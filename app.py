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
st.set_page_config(page_title="Traffic in Copenhagen",layout="wide")
st.title("How traffic spreads throughout Copenhagen")
st.caption("By Astrid Machholm and Julius Olander")

# introduction
st.write("Copenhagen is the city over half a million people call home, while over 62 million overnight stays are spent by tourists from around the world each year [1]. Citizens commuting to and from work and tourists exploring the city’s many blooming cultural and gastronomic locations present great logistical mobility challenges with regard to city infrastructure. As in many other cities, Copenhagen commuting is done by walking on foot, driving by car, and taking public transport such as buses and trains. But what makes Copenhagen truly special is its municipality’s massive efforts towards becoming “the world’s best bicycling city” as part of its strategy to become more carbon neutral, and reduce noise pollution and traffic bottlenecks, while furthering public health. On an average day, over 1.4 million kilometers are traveled by bike collectively, and the city houses over 745.000 bikes and more than 380 kilometers of bike lanes [2].")
st.write("In this article, we look at some of the publicly available data from the Copenhagen Municipality regarding traffic counts throughout the city. Through analysis of the data, we dive into tendencies in commuting to provide a basis for exploration that can support future decision-making and investments. The data spans 2009 to 2023 and includes manually counted observations of different transportation forms. The main focus is on the two primary forms of transportation, but it is also possible to explore other transportation forms used in the city, including pedestrians, electric scooters, buses, and more.")

# line chart
st.subheader("More cars in Copenhagen despite efforts to reduce heavy traffic in the city")

col11, col12 = st.columns([1,1])

col11.write("Public transportation is considered a sustainable choice for commuting, especially in Copenhagen, where the metro and S-trains are powered by electricity. Private cars are thus the bicycles' primary opponents in the battle for carbon neutrality. Figure 1 investigates bicycle and car intensity development on the roads through average observation counts, as well as the municipality's awareness of the traffic matter through the number of yearly manual data collection done on roads throughout the city.")
col11.write("When inspecting the average number of cars and bikes observed throughout the traffic counting stations, we see a rise in both, indicating a general increase in traffic intensity over the years. However, as the COVID-19 pandemic set in in 2020, the car and bike trends diverged. Car usage seemed to be unchanged by the lockdowns, remote working, and other factors at play at that time. For bikes, we see a slight dip as COVID hit in 2021, and interestingly, it takes a few years to recover to the pre-COVID positive trend. This is confirmed through other investigations by the municipality [3].  As society opened back up again in 2022, we see the positive trend continue to rise and reach an all-time high in 2023. We theorize that, culturally, a bike is an essential tool for commuting to work in Copenhagen. As remote work was implemented and workplaces and schools shut down, fewer people chose their bikes for commuting during spare-time activities. This suggests that bikes are often selected for work and school commuting over other commutes. Thus, the city municipality should ensure that the bicycle is further promoted as the most efficient way of getting to work or school on time while ensuring that biking hotspots during peak hours, like Dronning Louises Bro, Tagensvej, and H.C. Andersens Boulevard can efficiently disperse cyclists during peak-traffic hours, e.g. through the Grøn Bølge initiative where traffic lights prioritize bikes on select roads in peak-hours [5].")

col12.image("plots/plot_dual.png", caption="Figure 1: The upper chart shows the average number of bikes and cars per road observation per year. The numbers have been increasing over the years. The lower chart shows the number of times manual traffic observations have been done each year. Note that 2020 is the year with the fewest road counts, and in the years since, the number of traffic observations has tripled compared to pre-Covid times.")


# Moran's I
st.subheader("How biking citizens and the car owners of Copenhagen share the city")

st.write("Apart from understanding the intensity of traffic generally throughout the city, it is relevant to know how the traffic is spread in each area before deciding where and how to regulate traffic to achieve comfort for citizens and the city's environmental aims. There are many famous measures, most notably is probably mean, median, variance, and standard deviation. However, these measures fall short of describing phenomena like: how does a given variable spread over a given shape/geography? Similar to the relationship between mean and median, various ways exist to answer this. We will focus on what is perhaps the simplest: Moran's I, to answer the question of how do bikes spread throughout the city. At one extreme, we would have bikes or cars exclusively placed in a particular area; at another, we would have bikes or cars spread out in small pockets. Understanding how this varies throughout the city of Copenhagen can help inform city planning decisions, explain why certain areas are better to bike in, hint at what spaces are most shared between people, and more. Moran's I thus becomes interesting for both the hypothetical city planner and, more importantly, the biking citizenry of Copenhagen.")
st.write("Moran's I is a statistical measure with a value from -1 to 1. If an area has a Moran's I of -1, it means that the bikes/cars are perfectly scattered. Analogously, one can think of a chess board where all dark tiles (i.e., the high number of observed bikes/cars) are completely surrounded by light tiles (the low number of observed bikes/cars). On the other extreme, where Moran's I is equal to 1, the light and dark tiles are divided into two perfect clusters. In other words, low-value areas have cars and bikes spread out, whereas high-value areas have cars and bikes close together in clusters.")
st.write("Regarding traffic in Copenhagen, areas with values closer to -1 can be interpreted as areas with light and scattered traffic. These areas are likely either used for everyday slow traffic, or perhaps the area might be dominated by scattered building blocks rather than a few highly visited areas. Areas with values closer to one indicate that only a few roads carry hefty traffic, e.g., Dronning Louises Bro, connecting areas that many people must get through on their daily commutes. These areas will be intensely packed and require more road safety and—in light of the municipality's bike strategy—prioritize bike speed and perhaps future infrastructure investments to expand the bike paths.")

col21, col22 = st.columns(2)

with col21:
   components.html(bike_string, height=470)

with col22:
   components.html(car_string, height=470)
   
st.caption("Figure 2: Map displaying the Moran's I value for each district of Copenhagen (excluding Frederiksberg). The left map is bikes, and the right map is cars. Note that the color scales on the two maps are not exactly the same.")

st.write("As seen in Figure 2 (right) and further unfolded in Figure 3 (bottom), the car traffic seems to go straight through the city from Østerbro, through Indre By, to Amager Vest. The further away from the inner city, the more scattered the traffic is, as seen in the four districts with negative Moran's I, most notable in Figure 3.")
st.write("Interestingly, for bikes, the areas with the highest Moran's I are also the areas with the highest population growth (mainly dominated by a young demographic) [6]. This indicates that many people in these areas use bikes to get to and from the same areas (e.g., university and work) using the same paths. In these areas, the bikes are close together on the bicycle lanes, so bikers share a limited space. Only two districts have negative bicycle Moran's I, and again, these are the areas furthest from Indre by, namely Vanløse and Brønshøj. Perhaps these areas are too far from the city to be efficiently connected for everyday bike commuting.")
st.write("On Amager Vest and Indre By, the most intense bike traffic might intersect with the most intense car traffic; thus, these areas are important to develop for road safety and efficiency. In connection with further studies into the uses of these areas of the city, it may be possible to determine strategies to limit car traffic in these intense areas to make biking more pleasant and to achieve the strategy of reducing cars. ")

left_co, cent_co,last_co = st.columns([1,6,1])

cent_co.image("plots/morans_bikes.png")
cent_co.image("plots/morans_cars.png", caption="Figure 3: Each district is depicted in the order of Moran's I (upper: bikes, lower: cars). The tiles are calculated based on the locations of road observation stations, and the color corresponds to the number of observed bikes/cars at each location. As the bicycles' Moran's I range higher, the clustering is most predominant here. Note how Amager Vest has a high number of observation bikes in a cluster on one side of the map/square and very few on the other. The opposite is observed in Vanløse and Brønshøj, where high and low observation counts are scattered between each other.")

# bar chart
st.subheader("The municipality's data collection needs improvement")
st.write("To expand upon Figure 1, we look at different means of transportation and how they have evolved over the years in Figure 4. Notably, almost all vehicles have very few normalized counts in 2020 relative to other years, so few that it can hardly be explained by the pandemic alone, or at least does not give a representative picture of the reality of traffic that year. It is instead likely just due to the means of data collection. As the municipality's \"traffic counts\" data is collected manually by people counting the traffic passing by, there likely just weren't many people stationed to carry out the counting during the year of the pandemic. The traffic may have been less, but the lack of data makes the numbers unreliable and unrepresentative. In 2019, we see how electric scooters suddenly occur for the first time. As the electric scooter was probably seen around the streets of Copenhagen before then, this indicated that novel means of transportation are added to the categories registered by the municipality when deemed relevant. After all, companies like Lime, Voi, and Tier have begun to dominate the landscape in Copenhagen, making use of the city's extensive bicycle infrastructure and providing alternative solutions to the otherwise tried and tested bicycle. If the municipality wants to continue developing bicycle infrastructure, such novel transportation methods must also be factors in decision-making.")

components.html(bokeh_string, height=780)
st.caption("Figure 4: Interactive chart showing the normalized observations of various means of transportation over the years. Most notably, 2020 is missing data, and the data collector only started recording electric scooters in 2019. Likewise, busses are also most prominent in the data in the most recent years, whereas we see a consistent upward trend in the use of cargo bikes. Select more categories and investigate the trends.")
st.write("The great increase in counts for 2022 and 2023 may suggest that the municipality is aware that an increased effort towards better data quality must be initiated to better understand the city's mobility trends to improve analysis and support decision-making towards achieving their carbon neutrality aims. However, to better understand spatio-temporal patterns in transportation, much more sophisticated means of data collection are needed. In the coming years, we recommend avoiding relying on sparse manual counts and shifting towards more sophisticated data collection methods, like user GPS data, to truly understand mobility patterns and trends [4].")

st.write("  ")
st.write("  ")
st.write("  ")
st.write("  ")

st.caption("Sources")
st.write("[1] https://www.visitdenmark.dk/corporate/videncenter/noegletal-om-dansk-turisme")
st.write("[2] https://byudvikling.kk.dk/mobilitet-og-cykling/verdens-bedste-cykelby")
st.write("[3] https://www.kk.dk/nyheder/cykling-i-koebenhavn-faldt-under-corona")
st.write("[4] https://videnskab.dk/teknologi/vild-visualisering-forskere-har-kortlagt-cykeltrafikken-i-koebenhavn/")
st.write("[5] Cykelfokus 2024, Københavns Kommunes retningslinjer for cykel- og vejprojekter, https://www.kk.dk/sites/default/files/agenda/03e7571c-7870-4344-95bf-6d33c5779242/81e1e2f8-dd62-415e-be0c-ea31526f3f0b-bilag-2.pdf")
st.write("[6] Nøgletal for København, Status på København 2020, Den Tværgående Analyseenhed, https://www.kk.dk/sites/default/files/2022-02/Status%20på%20København%202020.pdf")