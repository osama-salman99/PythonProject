from helper import *

print(get_language('en'))
data = get_pageview_data(r'..\res\pageviews-20210401-120000.txt')
for datum in data:
	print(datum)
