import matplotlib.pyplot as plt

from helper import *

# Scatter plot of average views per page for most and least viewed languages

dataframe = get_pageviews_data(r'..\res\pageviews-20210401-120000-sample.txt')
languages = dataframe['Language'].unique()
avgList = []
totalViews = []
numberOfPagesList = []
for language in languages:
	views = dataframe[dataframe['Language'] == language]['Views']
	numberOfPages = len(views)
	total = sum(views)
	print(language, numberOfPages, total, total / numberOfPages)
	avgList.append(total / numberOfPages)
	totalViews.append(total)
	numberOfPagesList.append(numberOfPages)
plt.scatter(numberOfPagesList, avgList)
plt.show()
