##import modules
import pandas as pd
import matplotlib.pyplot as plt

##read file and create dataframe
df = pd.read_csv("pageviews-20160801-000000", sep=" ", header=None)

##drop missing values and rename columns
df.dropna(inplace=True)
df.rename(columns={0: "Language", 1: "Article", 2: "Views", 3: "Size"}, inplace=True)

##extract lanuages from dataframe and store in list
languages = list(df.Language)

##split each language with it's language name and page location and store them in list
lang = []
page_loc = []
for lan in languages:
	if "." in lan:
		values = lan.split(".")
		lang.append(values[0])
		if values[1] == "b":
			page_loc.append("wikibooks")
		elif values[1] == "d":
			page_loc.append("wiktionary")
		elif values[1] == "m":
			page_loc.append("wikimedia")
		elif values[1] == "mw":
			page_loc.append("wikipedia mobile")
		elif values[1] == "n":
			page_loc.append("wikinews")
		elif values[1] == "q":
			page_loc.append("wikiquote")
		elif values[1] == "s":
			page_loc.append("wikisource")
		elif values[1] == "v":
			page_loc.append("wikiversity")
		elif values[1] == "w":
			page_loc.append("mediawiki")
		else:
			page_loc.append(values[1])

	else:
		lang.append(lan)
		page_loc.append("wikipedia ")

##insert new columns to dataframe and drop old language column
df.drop(columns=["Language"], inplace=True)
df.insert(0, "Language", lang)
df.insert(1, "Page_Location", page_loc)

##Draw different plots from dataframe
frame = df.groupby("Language").Views.sum().nlargest(10).to_frame().reset_index()
fig = plt.figure()
plt.bar(frame.Language, frame.Views)
plt.title("Top 10 Languages according to Views")
plt.xlabel('Language')
plt.ylabel('Views')
plt.show()

frame = df[df.Language == "af"].groupby("Page_Location").Views.sum().to_frame().reset_index()
fig = plt.figure()
plt.bar(frame.Page_Location, frame.Views)
plt.title("Total Views of all locations of Language(af)")
plt.xlabel('Page Location')
plt.ylabel('Views')
plt.show()

frame = df.groupby("Page_Location").Views.sum().to_frame().reset_index()
fig = plt.figure()
fig.set_figheight(50)
fig.set_figwidth(170)
plt.bar(frame.Page_Location, frame.Views)
plt.title("Total Views of all locations")
plt.xlabel('Page Location')
plt.ylabel('Views')
plt.show()
