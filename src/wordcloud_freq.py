from wordcloud import WordCloud
from helper import *
import matplotlib.pyplot as plt

dataframe = get_pageviews_data(r'..\res\pageviews-20210401-120000-sample.txt')
dataframe = dataframe[dataframe['Page Title'] == 'YouTube']
print(dataframe)

frequencies = {}
for language in dataframe['Language']:
	frequencies[language.replace(',', '')] = dataframe[dataframe['Language'] == language]['Views'].iloc[0]

wordCloud = WordCloud(width=500, height=500, background_color='white', min_font_size=10, relative_scaling=0	) \
	.generate_from_frequencies(frequencies)

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordCloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig(r'../output/wordcloud.png')
# plt.show()
