import matplotlib.pyplot as plt

from helper import *

dataframe = get_pageviews_data(r'..\res\pageviews-20210401-120000.txt')
languages = dataframe['Language'].unique()

data = []
for language in languages:
	sortedViews = dataframe[dataframe['Language'] == language].sort_values('Views', ascending=False)['Views']
	totalViews = sum(sortedViews)
	mostViewed = sortedViews.iloc[0]
	otherViews = totalViews - mostViewed
	data.append([language, mostViewed, totalViews, otherViews])
	print(language, mostViewed, totalViews, otherViews)
data = pd.DataFrame(columns=['Language', 'Most Viewed', 'Total Views', 'Other Views'], data=data)
data = data.sort_values('Total Views', ascending=False).head(7)
fig, ax = plt.subplots()
languages = data['Language']
otherViews = data['Other Views']
mostViewed = data['Most Viewed']
ax.bar(languages, otherViews, label='All Other Views')
ax.bar(languages, mostViewed, label='Most Viewed Page', bottom=otherViews)
plt.title('Most viewed page ratio for top 7 most viewed languages')
plt.legend()
plt.savefig(r'..\output\most_page_viewed_ratio.png')
plt.show()
