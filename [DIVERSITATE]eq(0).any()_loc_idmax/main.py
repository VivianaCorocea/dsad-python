import pandas as pd

#cerinta 1
localitati_df = pd.read_csv("Coduri_Localitati.csv")
diversitate_df = pd.read_csv("Diversitate.csv")

coloane_ani = ["2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"]

gauri_zero = diversitate_df[coloane_ani].eq(0).any(axis=1)

localitati_cu_zero = diversitate_df[gauri_zero].copy()
localitati_cu_zero.rename(columns={"Localitate":"City"}, inplace=True)

localitati_cu_zero.to_csv("Cerinta1.csv", index=False)

#cerinta2
diversitate_cu_medie_df = diversitate_df.copy()

diversitate_cu_medie_df["DiversitateMedie"] = diversitate_cu_medie_df[coloane_ani].mean(axis=1)

merged_df = pd.merge(localitati_df[["Siruta", "Judet", "Localitate"]],
                     diversitate_cu_medie_df[["Siruta","DiversitateMedie"]], on="Siruta", how="inner")

merged_df = merged_df.loc[merged_df.groupby(by="Judet")["DiversitateMedie"].idxmax()]
print(merged_df)
merged_df.rename(columns={"DiversitateMedie":"Diversitate Maxima"}, inplace=True)

merged_df.drop(columns=["Siruta"], inplace=True)
merged_df = merged_df.sort_values("Diversitate Maxima", ascending=False)

merged_df.to_csv("Cerinta2.csv", index=False)