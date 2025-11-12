import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
# by hamMUSings 11/25

df = pd.read_csv('space_weather_conds.csv')

# Initialize figure with subplots
fig = make_subplots(
    rows=22, cols=9,
    specs=[[None,None,None,None,None,None,None,None,None],
           [None,None,None,None,None,None,None,None,None],
           [{"type": "indicator", "rowspan": 3, "colspan": 3},None,None,{"type": "indicator","rowspan": 3, "colspan": 3},None,None,{"type": "indicator","rowspan": 3, "colspan": 3},None,None],
           [None,None,None,None,None,None,None,None,None],
           [None,None,None,None,None,None,None,None,None],
           [None,None,None,None,None,None,None,None,None],
           [None,None,None,None,None,None,None,None,None],
           [{"type": "indicator", "rowspan": 3, "colspan": 3},None,None,{"type": "indicator", "rowspan": 3, "colspan": 3},None,None,{"type": "indicator", "rowspan": 3, "colspan": 3},None,None,],
           [None,None,None,None,None,None,None,None,None],
           [None,None,None,None,None,None,None,None,None],
           [None,None,None,None,None,None,None,None,None],
           [None,{"type": "scatter", "rowspan": 6, "colspan": 2},None,{"type": "Scattergeo", "rowspan": 6, "colspan": 3},None,None,{"type": "bar", "rowspan": 6, "colspan": 1},{"type": "bar", "rowspan": 6, "colspan": 1},None],
           [None,None,None,None,None,None,None,None,None],
           [None,None,None,None,None,None,None,None,None],
           [None,None,None,None,None,None,None,None,None],
           [None,None,None,None,None,None,None,None,None],
           [None,None,None,None,None,None,None,None,None],
           [None,None,None,None,None,None,None,None,None],
           [None,None,None,None,None,None,None,None,None],
           [None,{"type": "table","rowspan": 3, "colspan": 7},None,None,None,None,None,None,None],
           [None,None,None,None,None,None,None,None,None],
           [None,None,None,None,None,None,None,None,None]
           ]
)

##########################################################
# Gauge for K-Index
##########################################################
fig.add_trace(
    go.Indicator(
    mode="gauge+number",
    value=df['kindex'].iloc[0],
    title={'text': "K-Index (K)"},
    gauge={'axis': {'range': [0, 9]},  # Set the range from 0 to 100
           'bar': {'color': "white"},
           'bgcolor': "white",
           'borderwidth': 2,
           'bordercolor': "gray",
           'steps': [
               {'range': [0, 1], 'color': '#014D4E'},
               {'range': [1, 2], 'color': 'teal'},
               {'range': [2, 4], 'color': 'goldenrod'},
               {'range': [4, 9], 'color': 'lightgray'}
               ]
           }
    ),
    row=3, col=4
)
##########################################################
# Gauge for Solar Flux Index
##########################################################
fig.add_trace(go.Indicator(
    mode="gauge+number",
    value=df['sfi'].iloc[0],
    title={'text': "Solar Flux Index (SFI)"},
    gauge={'axis': {'range': [0, 300]},  # Set the range from 0 to 100
           'bar': {'color': "white"},
           'bgcolor': "white",
           'borderwidth': 2,
           'bordercolor': "gray",
           'steps': [
               {'range': [0, 70], 'color': 'lightgray'},
               {'range': [70, 90], 'color': 'goldenrod'},
               {'range': [90, 150], 'color': 'teal'},
               {'range': [150, 325], 'color': '#014D4E'}
               ]
           }
    ),
    row=3, col=1
)
##########################################################
# Gauge for A-Index
##########################################################
fig.add_trace(
go.Indicator(
    mode="gauge+number",
    value=df['aindex'].iloc[0],
    title={'text': "A-Index (A)"},
    gauge={'axis': {'range': [0, 100]},# Full scale 400  # Set the range from 0 to 100
           'bar': {'color': "white"},
           'bgcolor': "white",
           'borderwidth': 2,
           'bordercolor': "gray",
           'steps': [
               {'range': [0, 7], 'color': '#014D4E'},
               {'range': [7, 15], 'color': 'teal'},
               {'range': [15, 30], 'color': 'goldenrod'},
               {'range': [30, 100], 'color': 'lightgray'}] #400 real
           }
    ),
    row=3, col=7
)

##########################################################
# Map for Aurora Latitude Impact
##########################################################
# Get the latitude for the aurora from the the imported csv
aurora = df['lat'].iloc[0]

# Generate points for the longitude, from -180 to 180 degrees
lons = np.arange(-180, 181, 1)

# Generate latitude points for the aurora
aurora = [aurora] * len(lons)


fig.add_trace(
    go.Scattergeo(
        lon=lons,
        lat=aurora,
        mode='lines',
        line=dict(width=2, color='red'),
        name='Aurora'
    ),
    row=12, col=4
)

# Configure the map layout
fig.update_geos(
    resolution=110,
    showcoastlines=True,
    showcountries=True,
    showocean=True,
    oceancolor="LightBlue",
    showland=True,
    landcolor="LightGreen",
    projection_type = 'natural earth'
)
    
##########################################################
# Gauge for Solar Wind
##########################################################
fig.add_trace(
go.Indicator(
    mode="gauge+number",
    value=df['solarwind'].iloc[0],
    title={'text': "Solar Wind - km/s (SW)"},
    gauge={'axis': {'range': [0, 1000]},  # Set the range from 0 to 100
           'bar': {'color': "white"},
           'bgcolor': "white",
           'borderwidth': 2,
           'bordercolor': "gray",
           #'shape': "bullet",
           'steps': [
               {'range': [0, 500], 'color': 'teal'},
               {'range': [500, 1000], 'color': 'lightgray'}]
           }
    ),
    row=8, col=7
)
##########################################################
# Gauge for Sunspot Number
##########################################################
fig.add_trace(
    go.Indicator(
    mode="gauge+number",
    value=df['sunspot'].iloc[0],
    title={'text': "Sunspot Number (SN)"},
    gauge={'axis': {'range': [0, 250]},  # Set the range from 0 to 100
           'bar': {'color': "white"},
           'bgcolor': "white",
           'borderwidth': 2,
           'bordercolor': "gray",
           'steps': [
               {'range': [0, 50], 'color': 'lightgray'},
               {'range': [50, 100], 'color': 'goldenrod'},
               {'range': [100, 150], 'color': 'teal'},
               {'range': [150, 250], 'color': '#014D4E'}]
           }
    ),
    row=8, col=1
)
##########################################################
# Gauge for Aurora
##########################################################
fig.add_trace(
go.Indicator(
    mode="gauge+number",
    value=df['aurora'].iloc[0],
    title={'text': "Aurora (Aur)"},
    gauge={'axis': {'range': [0, 10]},# Full scale 400  # Set the range from 0 to 100
           'bar': {'color': "darkgray"},
           'bgcolor': "white",
           'borderwidth': 2,
           'bordercolor': "gray"
           }

    
    ),
    row=8, col=4
)
##########################################################
# Moving Bar for Signal Noise Level
##########################################################
noiseraw=df['signoise'].iloc[0]
noise_split=noiseraw.split("-", 1)

if len(noise_split) == 2:
    top=int(noise_split[0][1])
    bottom=int(noise_split[1][1])
else:
    top=int(noise_split[0][1])
    bottom=int(noise_split[0][1])

fig.add_trace(
    go.Scatter(x=[1, 2], y=[bottom, bottom],
        fill=None,
        mode='lines',
        line_color='darkgray',
        ),
        row=12, col=8
)

fig.add_trace(
    go.Scatter(
        x=[1, 2],
        y=[top, top],
        fill='tonexty', # fill area between trace0 and trace1
        mode='lines', line_color='darkgray'),
    row=12, col=8
)
# Update y-axis options
fig.update_yaxes(
    showline=True,
    linewidth=2,
    linecolor='lightgray',
    gridcolor='lightgray',
    range=[0, 9],
    row=12, col=8
)

# Update x-axis options
fig.update_xaxes(
    range=[1, 2],
    showline=True,
    linewidth=2,
    linecolor='lightgray',
    showticklabels=False,
    showgrid=False,
    title_text="Sig Noise Level<br>(S-Units)",
    title_font_weight='bold',
    title_font_size=10,
    row=12, col=8
)

##########################################################
# Scatter for X-Ray
##########################################################
# Extract data from the csv but also split it into letter and number parts
xraytotal= df['xraytotal'].iloc[0]
xraylet=xraytotal[0]
xraynum=float(xraytotal[1:])

# Based on letter part create the x axis data array
if xraylet == 'A':
    x_data = [xraynum,-1,-1,-1 , -1]
if xraylet == 'B':
    x_data = [-1,xraynum,-1,-1 , -1]
if xraylet == 'C':
    x_data = [-1,-1,xraynum,-1 , -1]
if xraylet == 'M':
    x_data = [-1,-1,-1,xraynum , -1]
if xraylet == 'X':
    x_data = [-1,-1,-1,-1 ,xraynum]


y_data= ['A', 'B', 'C', 'M', 'X']
custom_colors = {'A': '#014D4E', 'B': 'teal', 'C': 'goldenrod', 'M':'darkgray', 'X':'lightgray'}

# Create a figure with two traces
fig.add_trace(go.Scatter(x=x_data, y=y_data,mode='markers+text',marker_color='teal',text=xraytotal),row=12, col=2)

fig.update_traces(marker_size=20, row=12, col=2)

fig.update_xaxes(
    range=[0, 9.9],
    showgrid=True,
    showline=True,
    linewidth=2,
    linecolor='lightgray',
    gridcolor='lightgray',
    title_text="Hard X-Rays",
    title_font_weight='bold',
    title_font_size=10,
    showticklabels=False,
    row=12, col=2
)
fig.update_yaxes(
    showline=True,
    linewidth=2,
    linecolor='lightgray',
    gridcolor='lightgray',
    row=12, col=2
)

fig.update_traces(textposition='top center',row=12,col=2)

##########################################################
# Butterfly Bar for Bz  interplanetary magnetic field as impacted by solar activity
##########################################################
bzraw = df['magfield'].iloc[0]
# If it is positive put the value in the pos array and set negative to zero then vice versa for negative value
if bzraw >= 1:
    pos=[bzraw]
    neg=[0]
if bzraw < 1:
    pos=[0]
    neg=[bzraw]


bzbit = ['Bz']

fig.add_trace(
    go.Bar(x=bzbit, y=pos,
                base=0,
                marker_color='teal',
                name='Positive'),row=12, col=7
    )
fig.add_trace(
    go.Bar(x=bzbit, y=neg,
                marker_color='lightgray',
                name='Negative'),row=12, col=7
    )
fig.update_yaxes(
    range=[-50, 50],
    showline=True,
    linewidth=2,
    linecolor='lightgray',
    row=12, col=7
)
fig.update_xaxes(
    title_text="Interplanetary Mag<br>Field Sol Impact (Bz)",
    title_font_weight='bold',
    title_font_size=10,
    showline=True,
    linewidth=2,
    linecolor='lightgray',
    showticklabels=False,
    row=12, col=7
)

##########################################################
# Table for Electron Flux, Proton Flux, 304 Angstroms, And GeoMagnetic Field
##########################################################
#Inactive, Very Quite, Quiet, Unsettled, Active, Minor Storm, Major Storm, Severe Storm, or Extreme Storm

# Pulls the variables from the csv import
geoMAG=df['geomagfield'].iloc[0]
pFlux=df['pflux'].iloc[0]
eFlux=df['eflux'].iloc[0]
aNgs=df['heliumline'].iloc[0]

#Set the labels and label color for geomagnetic field
if geoMAG == 'INACTIVE':
    text_color = ['#014D4E','black','black','black']
    geoMAG='Inactive'
elif geoMAG == 'VR QUIET': #confirmed
    text_color = ['teal','black','black','black']
    geoMAG='Very Quiet'    
elif geoMAG == 'QUIET': #confirmed
    text_color = ['teal','black','black','black']
    geoMAG='Quiet'
elif geoMAG == 'UNSETTLD': #confirmed
    text_color = ['goldenrod','black','black','black']
    geoMAG='Unsettled'
elif geoMAG == 'ACTIVE': #confirmed
    text_color = ['goldenrod','black','black','black']
    geoMAG='Active'
elif geoMAG == 'MIN STRM':
    text_color = ['darkgray','black','black','black']
    geoMAG='Minor Storm'
elif geoMAG == 'MAJ STRM':
    text_color = ['darkgray','black','black','black']
    geoMAG='Major Storm'
elif geoMAG == 'SEV STRM': #confirmed
    text_color = ['lightgray','black','black','black']
    geoMAG='Severe Storm'
elif geoMAG == 'EXT STRM':
    text_color = ['lightgray','black','black','black']
    geoMAG='Extreme Storm'
else:
    text_color = ['black','black','black','black']
    geoMAG=geoMAG
    

fig.add_trace(
    go.Table(
        header=dict(
            values=['GeoMagnetic Field','Proton Flux (Pf)','Electron Flux (Ef)', '304 Angstroms (304A)'],
            line_color='white',
            fill_color='white',
            font=dict(size=18, family="Arial")
        ),
        cells=dict(
            values=[[geoMAG],[pFlux],[eFlux],[aNgs]],
            line_color='white',
            fill_color='white',
            font=dict(size=30, family="Arial",color=text_color)
        )
    )
    , row=20,col=2)
##########################################################
# All Sub-Plots
##########################################################
aurora_note=str(df['lat'].iloc[0])+"º"

fig.update_layout(
    annotations=[
        dict(
            x=0.5,
            y=0.18,
            text="Estimated Lowest Lat Impacted by Auroral Event",
            showarrow=False,
            font=dict(size=10, color="black", weight='bold'),
            xref='paper',
            yref='paper'
        ),
        dict(
            x=0.41,
            y=0.36,
            text=aurora_note,
            showarrow=False,
            font=dict(size=12, color="black", weight='bold'),
            xref='paper',
            yref='paper'
        )
    ]

)

plot_title= "Solar-Terrestrial Data @"+ df['date'].iloc[0]

fig.update_layout(
    showlegend=False,
    barmode='relative',
    plot_bgcolor="white",
    title=plot_title
)
#fig.show()
fig.write_image("./output/space_weather.png",width=1920, height=1080)



