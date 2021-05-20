import re
import pandas as pd

isoCodesFile = open(r'../res/iso_codes.txt', encoding='utf8')
isoCodes = {}


def init():
	for line in isoCodesFile.readlines():
		line = line.strip().split('\t')
		code = line[0]
		language = line[1]
		isoCodes[code] = language


init()


def get_language(code):
	try:
		return isoCodes[code]
	except KeyError:
		return code


def get_pageviews_data(filepath):
	file = open(filepath, encoding='utf8')
	pageviews = []
	for line in file.readlines():
		line = line.strip().split(' ')
		pageviews.append(PageView(line[0], line[1], line[2]))
	data = []
	for edit in pageviews:
		data.append(edit.as_list())
	return pd.DataFrame(data, columns=['Language', 'Projects', 'Page Title', 'Views']), pageviews


def get_geoeditors_data(filepath):
	file = open(filepath, encoding='utf8')
	geoEditors = []
	for line in file.readlines():
		line = line.strip().split('\t')
		geoEditors.append(GeoEdit(line[0], line[1], line[2], line[3], line[4]))
	data = []
	for edit in geoEditors:
		data.append(edit.as_list())
	return pd.DataFrame(data, columns=['Language', 'Country', 'Activity', 'Lower Bound', 'Upper Bound']), geoEditors


def get_unique_devices_per_domain_data(filepath):
	file = open(filepath, encoding='utf8')
	uniqueDevices = []
	for line in file.readlines():
		line = line.strip().split('\t')
		uniqueDevices.append(UniqueDomainAccess(line[0], line[1], line[2], line[3]))
	data = []
	for uniqueDevice in uniqueDevices:
		data.append(uniqueDevice.as_list())
	return pd.DataFrame(data, columns=['Language', 'Project', 'Under Estimate', 'Estimate', 'Offset']), uniqueDevices


def get_unique_devices_per_project_data(filepath):
	file = open(filepath, encoding='utf8')
	uniqueDevices = []
	for line in file.readlines():
		line = line.strip().split('\t')
		uniqueDevices.append(UniqueProjectAccess(line[0], line[1], line[2], line[3]))
	data = []
	for uniqueDevice in uniqueDevices:
		data.append(uniqueDevice.as_list())
	return pd.DataFrame(data, columns=['Project', 'Under Estimate', 'Estimate', 'Offset']), uniqueDevices


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
		self.language = get_language(language)
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

	def as_list(self):
		return [self.language, self.projects, self.page_title, self.number_of_views]

	def __repr__(self):
		return self.language + '\t' + str(self.projects) + '\t' + self.page_title + '\t' + str(self.number_of_views)


class GeoEdit:
	def __init__(self, language, country, activity, lower_bound, upper_bound):
		language = language.replace('wiki', '')
		self.language = get_language(language)
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

	def as_list(self):
		return [self.language, self.country, self.activity, self.lowerBound, self.upperBound]

	def __repr__(self):
		return self.language + '\t' + self.country + '\t' + self.activity + '\t' + str(self.lowerBound) + '\t' + str(
			self.upperBound)


class UniqueDomainAccess:
	def __init__(self, domain, underestimate, estimate, offset):
		splitDomain = domain.split('.')
		lanCode = splitDomain[0]
		language = get_language(lanCode)
		if language == lanCode:
			language = None
		self.project = splitDomain[-2]
		self.language = language
		self.underestimate = int(underestimate)
		self.estimate = int(estimate)
		self.offset = int(offset)

	def get_project(self):
		return self.project

	def get_under_estimate(self):
		return self.underestimate

	def get_estimate(self):
		return self.estimate

	def get_offset(self):
		return self.offset

	def as_list(self):
		return [self.language, self.project, self.underestimate, self.estimate, self.offset]

	def __repr__(self):
		return self.language + '\t' + self.project + '\t' + self.underestimate + '\t' + self.estimate + '\t' + self.offset


class UniqueProjectAccess:
	def __init__(self, project, underestimate, estimate, offset):
		self.project = project
		self.underestimate = int(underestimate)
		self.estimate = int(estimate)
		self.offset = int(offset)

	def get_project(self):
		return self.project

	def get_underestimate(self):
		return self.underestimate

	def get_estimate(self):
		return self.estimate

	def get_offset(self):
		return self.offset

	def as_list(self):
		return [self.project, self.underestimate, self.estimate, self.offset]

	def __repr__(self):
		return self.project + '\t' + str(self.underestimate) + '\t' + str(self.estimate) + '\t' + str(self.offset)
