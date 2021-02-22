# "Surfs Up" - Advanced Storage and Data Retrieval

Analysis of temperature and precipitation data from 9 weather stations in Hawaii

# Project Overview

The aim of this project is to analyze weather data in Hawaii to determine temperature and precipitation patterns throughout the past year. The purpose is to inform a local investor who wants to learn more about the weather before committing to open a shop selling surfing products and ice cream in Oahu. SQLite and SQLAlchemy are used to analyze the weather data and a climate app built in Flask to easily share the results of the analysis with investors. 

To get more detailed information about the temperature trends the investor wants to know specifically about the temperature trends for the months of June and Decemeber in Oahu, to see if the business would be sustainable year-round.

# Resources

Data used: [hawaii.sqlite](https://github.com/jkenning/Surfs_up/blob/main/hawaii.sqlite)

Software used: Python 3.7.9, Jupyter Notebook 6.1.4, Anaconda 1.10.0, Visual Studio Code 1.53.2

App created: [app.py](https://github.com/jkenning/Surfs_up/blob/main/app.py)

# Initial Analysis of Annual Data

One of the primary concerns of the investor is precipitation. Precipitation was plotted over the course of the last year of available data. Summary statistics show a maximum of 6.7, minimum of 0, mean of 0.18, and a standard deviation of 0.46; suggesting Oaha could indeed be a good location for the shop due to generally lower levels of precipitation.

![](https://github.com/jkenning/Surfs_up/blob/main/Resources/Precipitation.PNG)

Figure 1. Precipitation for the most recent year of data

Temperature observations were analyzed from the recording station closest to the proposed shop location (USC00519281) and plotted as a histogram. From the plot it can be inferred that the vast majority of observations made were over 67 degrees. Summary statistics indicate a maximum of 85, minimum of 54, and mean of 72 degrees, which is a positive indicator for the area being mostly suitable temperatures for the shop to be successful. 

![](https://github.com/jkenning/Surfs_up/blob/main/Resources/Temps_for_past_year_at_USC00519281.PNG)

Figure 2. Plot of temperature data from station USC00519281

# Results for June and December

The date collumn of the measurements table in the SQLite database was then filtered to retrieve temperatures for June and Decemeber specifically to get a better idea of whether the business would be sustainable in both the summer and winter year-round:

![](https://github.com/jkenning/Surfs_up/blob/main/Resources/June_temps_df.PNG)

Figure 3. Summary statistics for tempatures for the month of June

![](https://github.com/jkenning/Surfs_up/blob/main/Resources/June_temperatures.PNG)

Figure 4. Plot of temperatures for the month of June 

![](https://github.com/jkenning/Surfs_up/blob/main/Resources/December_temps_df.PNG)

Figure 5. Summary statistics for tempatures for the month of December

![](https://github.com/jkenning/Surfs_up/blob/main/Resources/December_temperatures.PNG)

Figure 6. Plot of temperatures for the month of December 

**Key observations:**

* There is minimal difference in average temperature which is only slightly higher in June (75°F) compared to December (71°F)

* There is also little overall difference between the maximum temperatures recorded in June (85°F) versus December (83°F)

* There is a somewhat larger difference in minimum temperature, with the value recorded in June (64°F) about eight degrees higher than in Decemeber (56°F)

# Summary

The main findings suggest that while both June and December have warm temperatures that could be suitable for business, the temperatures in June are more consistently high. There is a larger spread in the range of temperatures in December and there are likely more times during the month where the more variable weather is not good enough for surfing or ice cream. The larger standard deviation in the data for Decemeber (3.75) versus June (3.25) reflects this. 

## Further queries that could be performed

* The analysis only focuses on two months, more should be analyzed in a similar manner to see if there are other times of year where weather could be poor, or highly variable.

* Precipitation was listed as a key concern for the business and should be analyzed on an monthly scale as was done with temperature.

* How have temperatures and precipitation changed year-on-year? Weather could be very variable at certain times of the year and across different years due to a number of reasons, e.g. phases in global circulation patterns, risk of storm events, climate change etc. This includes how the weather is changing; is it expected to get better, worse, or stay the same in the future based on the forward-going trends determined from multiple years of previous data.

* How do temperature and precipitation relate to each other? It is possible you could have very warm days where it is also raining (and vice versa) which could make the weather unsuitable overall. It may need to be determined when it is both high temperature *and* low precipitation by plotting them together.

* We should consider examining data solely from the weather station closest to the shop location, but also compare this data to other stations which may have recorded different values depending on their location and geographic setting. Although, it may be that we would need to analyze data from all stations or other specific to get a better idea of what the weather is like and how it might vary across the region as a whole, not just the immediate vinicity of the shop.
