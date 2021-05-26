from helper import *
import matplotlib.pyplot as plt
import numpy as np

dataframe = get_unique_devices_per_domain_data(r'../res/unique_devices_per_domain_daily-2018-10-29.txt')
projects = list(dataframe['Project'].unique())[:5]
languages = list(dataframe['Language'].unique())

lanDict = {}
for language in languages:
	lanDict[language] = sum(dataframe[dataframe['Language'] == language]['Estimate'])
lanDict = dict(sorted(lanDict.items(), key=lambda item: item[1], reverse=True))
print(lanDict)
languages = list(lanDict.keys())
languages = languages[:10]
print(languages)

plt.figure(figsize=(8, 8))
plt.subplot(polar=True)
label_loc = np.linspace(start=0, stop=1.98 * np.pi, num=len(languages))
i = len(projects)
jump = 10
for project in projects:
	select = dataframe[dataframe['Project'] == project]
	values = []
	for language in languages:
		language = select[select['Language'] == language]['Estimate']
		values.append(sum(language))
	total = sum(values)
	if not total == 0:
		values = [value / total for value in values]
	left = jump * i
	right = jump * (i + 1)
	values = [((right - left) * value) + left for value in values]
	i -= 1
	print(project, values)
	plt.plot(label_loc, values, label=project)
plt.title('Projects unique visitors per language comparison', size=20)
lines, labels = plt.thetagrids(np.degrees(label_loc), labels=languages)
plt.legend(loc='lower center')
plt.savefig(r'../output/radar_chart.png')
plt.show()
