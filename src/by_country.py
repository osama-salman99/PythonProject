from helper import *
import pycountry
import plotly.express as px
import pandas as pd

dataframe = get_geoeditors_data(r'../res/geoeditors-monthly-2021-03.tsv')
countries = dataframe['Country'].unique()
data = pd.DataFrame(columns=['Country', 'ISOs', 'Editors'])
for country in countries:
	iso = country
	try:
		countryData = pycountry.countries.search_fuzzy(country)
		iso = countryData[0].alpha_3
	except LookupError:
		print(f'Could not find ISO for {country}')
		pass
	row = {'Country': country,
		   'ISOs': iso,
		   'Editors': sum(dataframe[dataframe['Country'] == country]['Upper Bound'])}
	data = data.append(row, ignore_index=True)
data['Editors'] = data['Editors'].astype(int)
fig = px.choropleth(data_frame=data,
					locations='ISOs',
					color='Editors',
					hover_name='Country',
					color_continuous_scale='RdYlGn')
fig.show()
