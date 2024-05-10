# Social Data Viz

## Introduction

This project sets out to investigate the development in bicycle usage in Copenhagen from the year 2009 to 2023 in the light of Københavns Kommune's strategy to become carbon neutral[2]. The analysis focuses on the amount of bicycle transport occuring the the city, partially on the bicycle infrastructure and the recourse allocation by the municipality towards monitoring of the bicycle trafic.

Hence, this project seeks to answer the following question:

**Insert research question**

Biking as part of daily city life, culture and climate/environmental policy has been an increasing focus area for the municipality. It is evident not only in media, but also in the biking data available.

Note: See how they’ve increased their counting over the years. It’s a clear strategy.

Understanding how people move through the city provides interesting insights into how the infrastructure can be further developed both for trafic efficiency and the citizens' enjoyment.

We are investigating how the number of bikes and vehicles has changed/remained over the time period recorded in the data, and finally—and maybe most interestingly—how these means of transportation is distributed in the city’s regions and the spacial autocorrelation of such regions, known as the Moran’s I.

The dataset is complex as it is both geospatial *and* temporal. This provides multiple interesting possible insight, meanwhile imposing challenges. The time series aspect makes it inappropriate to analyse all entries in the dataset together, and the geospatial component makes regional data sparse. Through our preprocessing and analysis, we try to account for these challenges. At the end of the report, we discuss the insights and shortcomings of our analysis, and the quality of the data and how this lends itself to the medium of visual narratives.

The end product (available on www.) aims to povide easily accessable information for a non-technical audiance among the interested parties involved in acheiving the municipality's environmental strategy. The intended audience is brought, including municipality employees of varying backgrounds, focus groups and more, and hence the visualisations and context displayed on the website aims to be easily understood without much prior understanding of technical jargon and statistical terms.

To limit confusion between the submitted websites as part of this course, we also provide the link to assignment 2's website: https://juliusolander.github.io/jekyll/update/2024/03/29/assignment-2.html

[1] https://www.opendata.dk/city-of-copenhagen/trafiktal

[2] Insert source to the municipality's strategy

## Data

`trafiktaelling.csv` has three intersting columns: geometry, date, and bike counts.
That will be the focus of story.

In the following analysis and visualisation, we will use the Trafiktælling data set from Københavns Kommune[1]. The data set spans the period from 2009 to 2023. The data is recordings of trafic on selected roads throughout Copenhagen, some days are frequently recorded whilest the majority of roads only have one data point in the entire data set. Each record in the data set describes multiple attributes; most relevant to us are the location (vejnavn, beskrivelse, husnummer), number of recorded cars and their subcategories (ktj_7_19, tung_pct).

The data set is limited in size with only 1147 number of rows. However, its 37 attributes covers many interesting and relevant aspects for the question at hand in the project. Many attributes have poorly explained names, thus we will explain all attributes that might be used throughout the analysis.

_7_9 is written behind many attribute names. This is to indicate that the count occured between 07:00 in the morning and 19:00 at night.

The colcumn titled "beskrivelse" most oftens describes where on the street the count occured. Notably, the describtions also shows in inconsistencies in the data. Sometimes they are tagged with e.g. "FOD" or "fodgængertælling 7-21" indicating that this row in the data only captures a select subset of occurences, not including vehicles or bicycle traifc. Thus, the data require more thourough preprocessing.

The column "taelling_type" could potentially have helped understand some of the inconsistences in the data, however, there is insufficient documentation as to what the different labels entail, thus, this column is not for much use.

There are three main categories of transport: vehicles (named "ktj" or "koretojer" in the data), bicycles (named "cykler"), pedestrians (named "fod"), lastbiler, elloebehjul, andre_busser.

The prefix "aadt" used on the recorded transportation types stand for the calculated Annual Average Daily Traffic. This number is relevant to our analysis. However, we are unable to find documentation describing how they calculate this anual average, which may lead to inacuracies in our interpretation of the number and thereby our analysis and conclusions.

This other prefix used, "hvdt", is not described at all in the documentation, hence, we do not know that this means and we cannot use these attributes.

The exact date for the data collection is captured in taelle_dato and for simplicity, the column aar only contains the year.

The exact location is captured in column "wkb_qoemetry". Each entry in the data set is a trafic count that occured on a specif day. These counts not only occured on a steet, but on a specific location on that street; hence, the geo tags associated with a specific street that's been counted on multiple days might differ. In the data, the geographical location is contained in a single value. Therefore, we must create seperate columns for the longditude and laditude as seen in the following block.

## Genre
The overall genre of our product is the *magazine style*. We have chosen this format explicitly becuase the data and analysis we are communicating is rather technical for our audience, hence guidance and explanation is necessary to help the viewer gain valuable information from our analysis. Complicated and/or technical matters can be rather inexcessible to an untrained, general audience if presented soley in a written format or as visualisations that require preexisting knowledge. When combining the two mediums, an untrained viewer can quickly gain an understanding of a new concept and use it to draw new conclusions.

**Visual Narrative**

*Highlighting:* Our format only lends itself well to the feature distinction tool. We have used this in the different coloring and shapes.

*Visual structuring:* Due to the genre specific communication method in the magazine style, we do not use any significant form of visual structuring. The text is the main guiding point for the reader, hence seperate visual ques to quide the reader would be redundant or even disturbing to the reader that is processing not only new information but also learning new technical measures.

*Transition guidance:* For the same reasons that we do not use visual structuring, we do not use transition guidance. All or information is contained on one page, hence we reader do not need ques to guide their attention from one scene to anotherm; there simply aren't any significant transitions to be guided through.

**Narrative Structure**

*Ordering:* First and foremost, the structuring is linearly ordered in the sense that the viewer reads from the top and is, initially, expected to inspect that visualisations in the order they appear in the text. However, the format also allows for a bit of random access; as the methods use in the analysis will be new to many receivers of our product, we expect and invite the readers to revisit explanatory text as needed. An example of such an invitation is the information boxes explaining statistical methods (e.g. the box explaining Moran's I).

*Interactivity:* The final visualisation we present can be seen as a summary of the partial finding presented in the alle the other (static) visualisations and the text. We allow the reader to synthasise their knowledge and explore the findings by providing them with an interactive visualisation. They can hover and highlight and filter over time. 

*Messaging*: Our final product (the website) combines the visualisations with explanatory texts, reference articles and other sources, and make use of annotations, introductory text and a final synthasis

## Analysis
There are many famous measures, most notably is probably mean, median, variance, and standard deviation. However, these measures fall short of describing phenomena like: _how_ does a given variable spread over a given shape/geography. Similar to the relationship between mean and median, there are various ways to answer this. We will focus on what is perhaps the simplest: Moran's I, to answer the question, how does bikes spread throughout the city. At one extreme, we would have bikes exclusively placed in a certain area, at another extreme, we would have bikes spread out in small pockets. Understanding how this varies throughout the city of Copenhagen can help inform city planning decisions, explain why certain areas are better to bike in, hint at what spaces are most shared between people, and more. Moran's I thus becomes intersting for both the hypothetical city planner and, more importantly, the biking citizenry of Copenhagen.

## Visualization
0. Explaining the Moran's I (chessboard or two sections)
1. Plot 1
2. Plot 2
3. Interactive plot that shows the main point

## Discussion
# social_data_viz
