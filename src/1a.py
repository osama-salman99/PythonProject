from helper import *

print(get_language('en'))
data = read_geoeditors_data(r'..\res\geoeditors-monthly-2021-03.tsv')
i = 0
for datum in data:
	print(datum)
	if i > 500:
		break
	i += 1
