##import modules
import pandas as pd
import matplotlib.pyplot as plt

##read file and create dataframe and rename columns
df = pd.read_csv("geoeditors-monthly-2019-04.tsv", sep="\t", header=None)
df.rename(columns={0: "Code_Name", 1: "Country", 2: "Edits", 3: "Min_Editors", 4: "Max_Editors"}, inplace=True)

##draw different plots
frame = df.groupby("Code_Name").Country.count().nlargest(10).to_frame().reset_index()
fig = plt.figure()
plt.bar(frame.Code_Name, frame.Country)
plt.title("Top 10 Wikipedia's according to no of Countries")
plt.xlabel('Code_Name')
plt.ylabel('No of Countries')
plt.show()

frame = df[df.Code_Name == "enwiki"].groupby("Country").Min_Editors.sum().nlargest(10).to_frame().reset_index()
fig = plt.figure()
fig.set_figheight(12)
fig.set_figwidth(70)
plt.pie(frame.Min_Editors, labels=frame.Country)
plt.legend(title="Country")
plt.title("Top 10 Countries with highest number of Min Editors in English Wikipedia")
plt.show()

frame = df[df.Code_Name == "enwiki"].groupby("Country").Max_Editors.sum().nsmallest(10).to_frame().reset_index()
fig = plt.figure()
fig.set_figheight(12)
fig.set_figwidth(70)
plt.pie(frame.Max_Editors, labels=frame.Country)
plt.legend(title="Country")
plt.title("Top 10 Countries with Lowest number of Max Editors in English Wikipedia")
plt.show()
