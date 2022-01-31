import pandas as pd
from prophet import Prophet
import plotly
from prophet.plot import plot_plotly, plot_components_plotly
import matplotlib.pyplot as plt 
from plotly import graph_objs as go

# June - November 2020 Dataset
df = pd.read_csv('covid19-may-october_2020.csv')

# January 2021 - June 2021 Dataset
#df = pd.read_csv('covid19-january-june_2021.csv')

# July - January 2020 Dataset
#df = pd.read_csv('covid19-july-december_2020.csv')

df.head()

# November 2021 Case Counts
df2 = pd.read_csv('covid19-may-november_2020.csv')

# July 2021 Case Counts
#df2 = pd.read_csv('covid19-january-july_2021.csv')

# January 2020 Case Counts
#df2 = pd.read_csv('covid19-july-january_2020.csv')

date = df2['ds']
casecounts = df2['y']

#m = Prophet(daily_seasonality=True)
m = Prophet()
m.add_country_holidays(country_name='CA')
m.fit(df)
future = m.make_future_dataframe(periods=30)
future.tail()
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
#fig1 = m.plot_components(forecast)
fig2 = m.plot(forecast)
fig1 = go.Figure(
    data=[
	go.Scatter(
		x=forecast['ds'],
		y=forecast['yhat'],
		mode='lines',
		line={'color': 'blue'},
		name='Forecast'
		),
	go.Scatter(
		x=date,
		y=casecounts,
		mode='lines',
		line={'color': 'red'},
		name='Actual cases'
		),
	])
fig1.show()
fig2.show()
