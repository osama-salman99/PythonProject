import matplotlib.pyplot as plt

from helper import *

# Scatter plot of average views per page for most and least viewed languages

dataframe = get_pageviews_data(r'..\res\pageviews-20210401-120000.txt')
languages = dataframe['Language'].unique()
data = []
for language in languages:
	views = dataframe[dataframe['Language'] == language]['Views']
	numberOfPages = len(views)
	total = sum(views)
	avg = total / numberOfPages
	print(language, total, avg, numberOfPages)
	data.append([language, total, avg, numberOfPages])
languagesDataFrame = pd.DataFrame(columns=['Language', 'Total Views', 'Average Views', 'Number of Pages'],
								data=data)

# Most viewed languages
languagesDataFrame = languagesDataFrame.sort_values('Total Views', ascending=False)
print(languagesDataFrame)
data = languagesDataFrame.head(25)
print(data)
viewsSizes = data['Total Views'] / sum(languagesDataFrame['Total Views'])
plt.scatter(data['Number of Pages'], data['Average Views'], s=viewsSizes * 1000)
plt.xlabel('Number of pages')
plt.ylabel('Average views per page')
plt.title('Average views per page for most 25 viewed languages')
plt.savefig(r'..\output\avg_views_per_page_most.png')
plt.show()

# Least viewed languages
languagesDataFrame = languagesDataFrame.sort_values('Total Views', ascending=True)
print(languagesDataFrame)
data = languagesDataFrame[languagesDataFrame['Total Views'] > 100].head(25)
print(data)
viewsSizes = data['Total Views'] / sum(languagesDataFrame['Total Views'])
plt.scatter(data['Number of Pages'], data['Average Views'], s=viewsSizes * 10000000)
plt.xlabel('Number of pages')
plt.ylabel('Average views per page')
plt.title('Average views per page for least 25 viewed languages')
plt.savefig(r'..\output\avg_views_per_page_least.png')
plt.show()
