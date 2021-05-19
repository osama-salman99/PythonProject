import re

isoCodesFile = open(r'../res/iso_codes.txt', encoding='utf8')
isoCodes = {}


def init():
	for line in isoCodesFile.readlines():
		line = line.strip().split(' ')
		code = line[0]
		language = line[1]
		isoCodes[code] = language


init()


def get_language(code):
	return isoCodes[code]


def read_pageview_data(file_path):
	file = open(file_path, encoding='utf8')
	pageviews = []
	for line in file.readlines():
		line = line.strip().split(' ')
		pageviews.append(PageView(line[0], line[1], line[2]))
	return pageviews


def read_geoeditors_data(file_path):
	file = open(file_path, encoding='utf8')
	geoEditors = []
	for line in file.readlines():
		line = line.strip().split('\t')
		geoEditors.append(GeoEdit(line[0], line[1], line[2], line[3], line[4]))
	return geoEditors


class PageView:
	pattern = re.compile(r'[a-z]+(\.(b|d|m|mw|n|q|s|v|w))+$')
	projectsDict = {'b': 'wikibooks', 'd': 'wiktionary', 'm': 'wikimedia', 'mw': 'wikipedia mobile', 'n': 'wikinews',
					'q': 'wikiquote', 's': 'wikisource', 'v': 'wikiversity', 'w': 'mediawiki'}

	def __init__(self, language_code, page_title, number_of_views):
		language = language_code
		projects = ['wikipedia']
		match = PageView.pattern.match(language_code)
		if match:
			language_code = language_code.split('.')
			language = language_code[0]
			projects = []
			for project in language_code[1:]:
				projects.append(PageView.projectsDict[project])
		try:
			language = get_language(language)
		except KeyError:
			pass
		self.language = language
		self.language = language
		self.projects = projects
		self.page_title = page_title
		self.number_of_views = int(number_of_views)

	def get_language(self):
		return self.language

	def get_projects(self):
		return self.projects

	def get_page_title(self):
		return self.page_title

	def get_number_of_views(self):
		return self.get_number_of_views()

	def __str__(self):
		return self.language + '\t' + str(self.projects) + '\t' + self.page_title + '\t' + str(self.number_of_views)


class GeoEdit:
	def __init__(self, language, country, activity, lower_bound, upper_bound):
		language = language.replace('wiki', '')
		try:
			language = get_language(language)
		except KeyError:
			pass
		self.language = language
		self.country = country
		self.activity = activity
		self.lowerBound = int(lower_bound)
		self.upperBound = int(upper_bound)

	def get_language(self):
		return self.language

	def get_country(self):
		return self.country

	def get_activity(self):
		return self.activity

	def get_lower_bound(self):
		return self.lowerBound

	def get_upper_bound(self):
		return self.upperBound

	def __str__(self):
		return self.language + '\t' + self.country + '\t' + self.activity + '\t' + str(self.lowerBound) + '\t' + str(
			self.upperBound)
