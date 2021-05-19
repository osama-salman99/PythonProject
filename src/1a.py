from helper import *

print(get_language('en'))
data = get_pageview_data(r'..\res\pageviews-20210401-120000.txt')
i = 0
for datum in data:
	print(datum)
	if i > 500:
		break
	i += 1
