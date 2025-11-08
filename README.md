# hfcondsgraph-plotly Summary
This docker container reformats data from http://hamqsl.com⁠ to two png images to post on a website using plotly. It generates both images hourly after the start time of the container. It publishes the pngs to /home/plotly/output which in the example docker-compose.yaml is bound to the web image folder on the host for automatic updates to the website. This folder can be bound anywhere by changing the docker-compose.yaml volume.

# Example Images
## HF Conditions Summary
![Screenshot of summary hf conditions in a sunburst chart.](https://github.com/hamMUSings/hfcondsgraph-plotly/blob/main/example_images/hfconds.png)
## Space Weather
![Screenshot of a more detailed space weather conditions in mutiple subcharts.](https://github.com/hamMUSings/hfcondsgraph-plotly/blob/main/example_images/space_weather.png)

# How To Read images

The same color scale is used on all images:

1. ![Dark Teal Sample](https://github.com/hamMUSings/hfcondsgraph-plotly/blob/main/example_images/color_examples/darkteal.png) **Dark Teal** -- Ideal Condition
2. ![Teal Sample](https://github.com/hamMUSings/hfcondsgraph-plotly/blob/main/example_images/color_examples/teal.png) **Teal** -- Good Condition
3. ![Goldenrod Sample](https://github.com/hamMUSings/hfcondsgraph-plotly/blob/main/example_images/color_examples/goldenrod.png) **Goldenrod** -- Mediocre Condition
4. ![Lightgray Sample](https://github.com/hamMUSings/hfcondsgraph-plotly/blob/main/example_images/color_examples/lightgray.png) **Light Gray** -- Lousy Condition

> [!IMPORTANT]
> If there is no color on the graph then there no easily interpret-able range and/or there is no top end to the range.
> [!NOTE]
> Date and times on both graphs are in UTC.

## HF Conditions Sunburst
> [!NOTE]
> HF Conditions image date/time is representative of the time the script ran in the docker container.

The top half represents day conditions while the bottom half is the conditions at night.  The bands are ordered highest band on the left moving to the lower bands on the right. This is mirrored in both the day and night conditions. Each slice is colored with Teal, Goldenrod, or Light Gray depending on the estimated conditions.  All units are labeled as well.


## Space Weather 
> [!NOTE]
> Date is as reported by hamqsl.com and represents the date of the data.

### Gauge / Indicator Charts - Solar Flux Index, etc
Each indicator chart either has the scale in color behind the bar or the bar has a white background. If the indicator has a white background then bar is always gray and there is no easy range to map.

Note depending on the measure the dark teal may be at the top of the range or the bottom of the range but in either case dark teal indicates the ideal conditions.

### Hard X-Rays
This chart is read bottom left to top right in a zig-zag fashion.  The hard x-ray data point is combined letter and number to indicate the range.  The lowest letter is A and the highest is X. This is indicated on the y-axis. Within each letter range there is a secondary intensity of 0.0 - 9.9.  This is indicated on the x-axis.  So the lowest left position is A0.0 and the top right position is X9.9.  For example C1.2 has more impact than A9.9.  

The hard x-ray is plotted as a colored circle using the same color scale as all the other charts and is labeled with the current measure.

### Estimated Lowest Latitude Impacted By Auroral Event
This is a simple moving line on the map that displays the estimated lowest latitude that may be impacted by the aurora.  The exact latitude is annotated in equatorial Pacific Ocean

### Interplanetary Magnetic Field Solar Impact (Bz)
This graphs displays the intensity and direction Earth's magnetic field as impacted by solar activity.  Graphed above the center line (+) it is moving with the Earth's magnetic field and generally has little impact while below the center line (-) moves against the Earth's magnetic field and cancels it out -- potentially causing impact.  Any values above the center line are graphed as Teal and below are graphed as Light Gray -- indicating potential impact conditions.

### Signal Noise Level (S-Units)
This displays a band were the noise floor is estimated to be.  This is always graphed as Light Gray indicated the expected s-unit noise floor.  It implies anything below it will likely be noisy and lousy conditions. Above the bar is expected to be more usable.

### Geomagnetic Field
Summary of geomagnetic field conditions as reported by hamqsl.com. This is a category based label and is color coded accordingly.

### Proton Flux, Electron Flux,  304 Angstrom
These are simple display of the reported data values with no ranges or coloring to indicate quality or quantity. These are left to the user to evaluate on their own.

# Docker
Pre-built docker image available at  [Docker Hub](https://hub.docker.com/r/hammusings/hfconds-plotly-hourly-generator)

# For Detailed Explaination of Measures
Visit Paul's [excellent explanation page on hamqsl.com](https://www.hamqsl.com/solar2.html#usingdata)
