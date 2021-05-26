##import modules
import pandas as pd
import matplotlib.pyplot as plt

## read files for per_domain and create dataframe from each file
per_domain_1 = pd.read_csv("unique_devices_per_domain_daily-2017-04-01", sep="\t", header=None).drop(
	columns=[1, 3]).rename(columns={0: "Wiki_Projects_lang", 2: "Visit"})

per_domain_2 = pd.read_csv("unique_devices_per_domain_daily-2017-04-02", sep="\t", header=None).drop(
	columns=[1, 3]).rename(columns={0: "Wiki_Projects_lang", 2: "Visit"})
per_domain_3 = pd.read_csv("unique_devices_per_domain_daily-2017-04-03", sep="\t", header=None).drop(
	columns=[1, 3]).rename(columns={0: "Wiki_Projects_lang", 2: "Visit"})
per_domain_4 = pd.read_csv("unique_devices_per_domain_daily-2017-04-04", sep="\t", header=None).drop(
	columns=[1, 3]).rename(columns={0: "Wiki_Projects_lang", 2: "Visit"})
per_domain_5 = pd.read_csv("unique_devices_per_domain_daily-2017-04-05", sep="\t", header=None).drop(
	columns=[1, 3]).rename(columns={0: "Wiki_Projects_lang", 2: "Visit"})
per_domain_6 = pd.read_csv("unique_devices_per_domain_daily-2017-04-06", sep="\t", header=None).drop(
	columns=[1, 3]).rename(columns={0: "Wiki_Projects_lang", 2: "Visit"})
per_domain_7 = pd.read_csv("unique_devices_per_domain_daily-2017-04-07", sep="\t", header=None).drop(
	columns=[1, 3]).rename(columns={0: "Wiki_Projects_lang", 2: "Visit"})
per_domain_8 = pd.read_csv("unique_devices_per_domain_daily-2017-04-08", sep="\t", header=None).drop(
	columns=[1, 3]).rename(columns={0: "Wiki_Projects_lang", 2: "Visit"})
per_domain_9 = pd.read_csv("unique_devices_per_domain_daily-2017-04-09", sep="\t", header=None).drop(
	columns=[1, 3]).rename(columns={0: "Wiki_Projects_lang", 2: "Visit"})
per_domain_10 = pd.read_csv("unique_devices_per_domain_daily-2017-04-10", sep="\t", header=None).drop(
	columns=[1, 3]).rename(columns={0: "Wiki_Projects_lang", 2: "Visit"})

##Draw pie chart
frame = per_domain_1.groupby("Wiki_Projects_lang").Visit.sum().nlargest(10).to_frame().reset_index()
fig = plt.figure()
fig.set_figheight(12)
fig.set_figwidth(70)
plt.pie(frame.Visit, labels=frame.Wiki_Projects_lang)
plt.legend(title="Projects with Lang")
plt.title("Top 10 Languages with max vists", fontsize=20)
plt.show()

##calculate average from each dataframe
date = ["2017-04-01", "2017-04-02", "2017-04-03", "2017-04-04", "2017-04-05", "2017-04-06", "2017-04-07", "2017-04-08",
		"2017-04-09", "2017-04-10"]
average_visits = []
average_visits.append(per_domain_1[per_domain_1.Wiki_Projects_lang == "en.wikipedia.org"].mean().values[0])
average_visits.append(per_domain_2[per_domain_2.Wiki_Projects_lang == "en.wikipedia.org"].mean().values[0])
average_visits.append(per_domain_3[per_domain_3.Wiki_Projects_lang == "en.wikipedia.org"].mean().values[0])
average_visits.append(per_domain_4[per_domain_4.Wiki_Projects_lang == "en.wikipedia.org"].mean().values[0])
average_visits.append(per_domain_5[per_domain_5.Wiki_Projects_lang == "en.wikipedia.org"].mean().values[0])
average_visits.append(per_domain_6[per_domain_6.Wiki_Projects_lang == "en.wikipedia.org"].mean().values[0])
average_visits.append(per_domain_7[per_domain_7.Wiki_Projects_lang == "en.wikipedia.org"].mean().values[0])
average_visits.append(per_domain_8[per_domain_8.Wiki_Projects_lang == "en.wikipedia.org"].mean().values[0])
average_visits.append(per_domain_9[per_domain_9.Wiki_Projects_lang == "en.wikipedia.org"].mean().values[0])
average_visits.append(per_domain_10[per_domain_10.Wiki_Projects_lang == "en.wikipedia.org"].mean().values[0])

# plot line graph
fig = plt.figure()
fig.set_figwidth(15)
plt.title("10 Days visits on 'en.wikipedia.org'", fontsize=20)
plt.xlabel('Date', fontsize=15)
plt.ylabel('Avg Visit', fontsize=15)
plt.plot(date, average_visits)
plt.show()

## read files for per_domain and create dataframe from each file
per_project_1 = pd.read_csv("unique_devices_per_project_family_daily-2017-04-01", sep="\t", header=None).drop(
	columns=[1, 3]).rename(columns={0: "Wiki_Projects", 2: "Visit"})
per_project_2 = pd.read_csv("unique_devices_per_project_family_daily-2017-04-02", sep="\t", header=None).drop(
	columns=[1, 3]).rename(columns={0: "Wiki_Projects", 2: "Visit"})
per_project_3 = pd.read_csv("unique_devices_per_project_family_daily-2017-04-03", sep="\t", header=None).drop(
	columns=[1, 3]).rename(columns={0: "Wiki_Projects", 2: "Visit"})
per_project_4 = pd.read_csv("unique_devices_per_project_family_daily-2017-04-04", sep="\t", header=None).drop(
	columns=[1, 3]).rename(columns={0: "Wiki_Projects", 2: "Visit"})
per_project_5 = pd.read_csv("unique_devices_per_project_family_daily-2017-04-05", sep="\t", header=None).drop(
	columns=[1, 3]).rename(columns={0: "Wiki_Projects", 2: "Visit"})
per_project_6 = pd.read_csv("unique_devices_per_project_family_daily-2017-04-06", sep="\t", header=None).drop(
	columns=[1, 3]).rename(columns={0: "Wiki_Projects", 2: "Visit"})
per_project_7 = pd.read_csv("unique_devices_per_project_family_daily-2017-04-07", sep="\t", header=None).drop(
	columns=[1, 3]).rename(columns={0: "Wiki_Projects", 2: "Visit"})
per_project_8 = pd.read_csv("unique_devices_per_project_family_daily-2017-04-08", sep="\t", header=None).drop(
	columns=[1, 3]).rename(columns={0: "Wiki_Projects", 2: "Visit"})
per_project_9 = pd.read_csv("unique_devices_per_project_family_daily-2017-04-09", sep="\t", header=None).drop(
	columns=[1, 3]).rename(columns={0: "Wiki_Projects", 2: "Visit"})
per_project_10 = pd.read_csv("unique_devices_per_project_family_daily-2017-04-10", sep="\t", header=None).drop(
	columns=[1, 3]).rename(columns={0: "Wiki_Projects", 2: "Visit"})

##calculate average from each dataframe
average_visits = []
average_visits.append(per_project_1[per_project_1.Wiki_Projects == "wiktionary"].mean().values[0])
average_visits.append(per_project_2[per_project_2.Wiki_Projects == "wiktionary"].mean().values[0])
average_visits.append(per_project_3[per_project_3.Wiki_Projects == "wiktionary"].mean().values[0])
average_visits.append(per_project_4[per_project_4.Wiki_Projects == "wiktionary"].mean().values[0])
average_visits.append(per_project_5[per_project_5.Wiki_Projects == "wiktionary"].mean().values[0])
average_visits.append(per_project_6[per_project_6.Wiki_Projects == "wiktionary"].mean().values[0])
average_visits.append(per_project_7[per_project_7.Wiki_Projects == "wiktionary"].mean().values[0])
average_visits.append(per_project_8[per_project_8.Wiki_Projects == "wiktionary"].mean().values[0])
average_visits.append(per_project_9[per_project_9.Wiki_Projects == "wiktionary"].mean().values[0])
average_visits.append(per_project_10[per_project_10.Wiki_Projects == "wiktionary"].mean().values[0])

# draw line graph
fig = plt.figure()
fig.set_figwidth(15)
plt.title("10 Days visits on Wiktionary", fontsize=20)
plt.xlabel('Date', fontsize=15)
plt.ylabel('Avg Visit', fontsize=15)
plt.plot(date, average_visits)
plt.show()
