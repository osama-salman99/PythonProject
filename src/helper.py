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


def get_pageview_data(file_path):
	file = open(file_path, encoding='utf8')
	pageviews = []
	for line in file.readlines():
		pageviews.append(line.strip().split(' ')[0:3])
	return pageviews


class PageView:
	pattern = re.compile(r'[a-z]+\.(b|d|m|mw|n|q|s|v|w)$')
	projects = {'b': 'wikibooks', 'd': 'wiktionary', 'm': 'wikimedia', 'mw': 'wikipedia mobile', 'n': 'wikinews',
				'q': 'wikiquote', 's': 'wikisource', 'v': 'wikiversity', 'w': 'mediawiki'}

	def __init__(self, language_code, page_title, number_of_views):
		language = language_code
		project = 'wikipedia'
		if PageView.pattern.match(language_code):
			language_code = language_code.split('.')
			language = language_code[0]
			project = language_code[1]
		self.language = language
		self.project = project
		self.page_title = page_title
		self.number_of_views = number_of_views

	def get_language(self):
		return self.language

	def get_project(self):
		return self.project

	def get_page_title(self):
		return self.page_title

	def get_number_of_views(self):
		return self.get_number_of_views()
