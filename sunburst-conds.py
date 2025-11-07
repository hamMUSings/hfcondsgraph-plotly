import plotly.express as px
import pandas as pd
import datetime

x = datetime.datetime.now()
now= x.strftime("%a %b %d, %Y @ %I:%M %p")
# Create the title string using an f-string
plot_title = f"HF Conditions: {now} (UTC)"

#df = px.data.tips()
df = pd.read_csv('hfconds.csv')

fig = px.sunburst(df, path=['tod', 'band', 'cond_cat'], values='value', color ='cond_cat',
             color_discrete_map={
                "Poor": "LightGray",
                "Fair": "Goldenrod",
                "Good": "Teal",
		"(?)": "white"})
# Update the layout with the dynamic title
fig.update_layout(title=plot_title)
#fig.update_traces(sort=False, selector=dict(type='sunburst')) 
# Export the figure to an HTML file
#fig.write_html("my_plotly_graph.html")
fig.write_image("./output/hfconds.png")
