import plotly_express as px 
import pandas as pd 
df = pd.read_csv('covid19.csv')
fig = px.scatter(df,x='date',y='cases',color='country')
fig.show()