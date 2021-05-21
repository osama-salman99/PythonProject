from helper import *

dataframe = get_pageviews_data(r'..\res\pageviews-20210401-120000-sample.txt')
print('loaded')
pageTitles = dataframe['Page Title'].value_counts()
print(pageTitles)
