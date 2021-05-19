isoCodes = open(r'../res/iso_codes.txt', encoding='utf8')


def get_language(code):
	for line in isoCodes.readlines():
		line = line.strip().split(' ')
		isoCode = line[0]
		language = line[1]
		if code == isoCode:
			return language
	return None
