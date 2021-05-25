import matplotlib.pyplot as plt

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
