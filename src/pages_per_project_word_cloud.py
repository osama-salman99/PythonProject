import matplotlib.pyplot as plt
from wordcloud import WordCloud

from helper import *

dataframe = get_pageviews_data(r'..\res\pageviews-20210401-120000.txt')
projects = dataframe[~dataframe['Projects'].str.contains(r'\|')]['Projects'].unique()
dataDict = {}
for project in projects:
	dataDict[project] = (len(dataframe[dataframe['Projects'].str.contains(project)]))
dataDict = dict(sorted(dataDict.items(), key=lambda item: item[1], reverse=True))

plt.pie(dataDict.values())
circle = plt.Circle((0, 0), 0.7, color='white')
plt.gcf().gca().add_artist(circle)
plt.legend(dataDict.keys(), loc='lower left')
plt.title('Number of pages per project')
plt.savefig(r'../output/pages_per_project.png')
plt.show()

dataframe = get_pageviews_data(r'..\res\pageviews-20210401-120000.txt')
dataframe = dataframe[dataframe['Page Title'] == 'YouTube']
print(dataframe)

frequencies = {}
for language in dataframe['Language']:
	frequencies[language.replace(',', '')] = dataframe[dataframe['Language'] == language]['Views'].iloc[0]

wordCloud = WordCloud(width=500, height=500, background_color='white', min_font_size=10, relative_scaling=0) \
	.generate_from_frequencies(frequencies)

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordCloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig(r'../output/wordcloud.png')
plt.show()
