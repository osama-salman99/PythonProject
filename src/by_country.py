from helper import *
import pycountry
import plotly.express as px
import pandas as pd

dataframe = get_geoeditors_data(r'../res/geoeditors-monthly-2021-03.tsv')
countries = dataframe['Country'].unique()
data = pd.DataFrame(columns=['Country', 'ISOs', 'Value'])
for country in countries:
	iso = country
	try:
		countryData = pycountry.countries.search_fuzzy(country)
		iso = countryData[0].alpha_3
	except LookupError:
		pass
	row = {'Country': country,
		   'ISOs': iso,
		   'Value': sum(dataframe[dataframe['Country'] == country]['Upper Bound'])}
	data = data.append(row, ignore_index=True)
data['Value'] = data['Value'].astype(int)
fig = px.choropleth(data_frame=data,
					locations='ISOs',
					color='Value',
					hover_name='Country',
					color_continuous_scale='RdYlGn')
fig.show()
