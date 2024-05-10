# 02806 Social Data Analysis and Visualisation
## Final project report

**Link to website: https://traficph.streamlit.app**

**Group 51**

Julius Olander, s203225
Astrid Machholm, s222228

## Introduction and motivation

This project investigates the development and patterns in bicycle usage across Copenhagen from 2009 to 2023 in light of the municipality's strategy to become carbon neutral. The analysis focuses on the amount of bicycle transport occurring in the city, patterns that might influence the future bicycle infrastructure, and the municipality's recourse allocation towards monitoring bicycle traffic. Hence, this project seeks to answer the following question:

*How does the use of different means of transportation develop over time, and is there a detectable difference in how traffic moves through different districts of Copenhagen?*

Understanding how people navigate the city offers insights into how the infrastructure can be further developed, enhancing both traffic efficiency and citizen enjoyment. We are investigating how the number of bikes and vehicles has changed/remained over the period and, finally—and maybe most interestingly—how these means of transportation are distributed in the city's regions through the spacial autocorrelation of such regions, known as the Moran's I.

Many data sources could provide high-quality insights into our research question, e.g., machine vision systems, road sensors, and user GPS data. However, these sources are often either expensive to deploy at scale, or the data simply isn't available to the public (like the user data from Hövding helmets used in a 2022 study by DTU researcher[2]). Therefore, a partial aim of our project is to try to provide insights with far more scarce but publically available data. Hence, the following analysis and visualizations use the Trafiktælling data set from Copenhagen Municipality[1]. The data set spans the period from 2009 to 2023. The data are manual traffic recordings on select roads throughout Copenhagen; some roads appear frequently in the data, while the majority only have one record in the entire data set. Each record in the data set describes multiple attributes; the location, counts, and date are the most relevant to our analysis.

The dataset is complex as it is both geospatial *and* temporal, providing multiple interesting possible insights, although also imposing challenges. The time series aspect makes analyzing all entries in the dataset as one inappropriate, and the geospatial component makes regional data sparse. Through our preprocessing and analysis, we try to account for these challenges. At the end of the report, we discuss the insights and shortcomings of our study, the data quality, and how this lends itself to the medium of visual narratives.

The end product (available on https://traficph.streamlit.app) aims to provide easily accessible information for a non-technical audience among the interested parties involved in achieving the municipality's environmental strategy. The intended audience includes municipality employees of varying backgrounds, focus groups, and more. Hence, the visualizations and context displayed on the website aim to be easily understood with little prior understanding of technical jargon and statistical terms despite including a statistical test rarely known by the general public.

To limit confusion between the two submitted websites as part of this course, we also provide the link to assignment 2's website: https://juliusolander.github.io/jekyll/update/2024/03/29/assignment-2.html

**The report for this project can be found in notebook.ipynb**

Sources:
- [1] https://www.opendata.dk/city-of-copenhagen/trafiktal
- [2] https://videnskab.dk/teknologi/vild-visualisering-forskere-har-kortlagt-cykeltrafikken-i-koebenhavn/