import pandas as pd

localitati_df = pd.read_csv("Coduri_Localitati.csv")
diversitate_df = pd.read_csv("Diversitate.csv")

#cerinta1
diversitate_cu_zero = diversitate_df.copy()

coloane_numerice = ["2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"]

diversitate_cu_zero = diversitate_cu_zero[coloane_numerice].eq(0).any(axis=1)

diversitate_cu_zero = diversitate_df[diversitate_cu_zero]

diversitate_cu_zero.to_csv("Cerinta1.1.csv", index=False)

#cerinta2
localitati_copie_df = localitati_df.copy()
diversitate_copie_df = diversitate_df.copy()

diversitate_copie_df["DiversitateMedie"] = diversitate_copie_df[coloane_numerice].mean(axis=1)

merge_df = pd.merge(localitati_copie_df[["Siruta", "Judet", "Localitate"]],
                    diversitate_copie_df[["Siruta","DiversitateMedie"]], on="Siruta", how="inner")

merge_df = merge_df.loc[merge_df.groupby(by="Judet")["DiversitateMedie"].idxmax()]

merge_df.rename(columns={"DiversitateMedie":"Diversitate Maxima"}, inplace=True)

merge_df.drop(columns=["Siruta"], inplace=True)

merge_df.to_csv("Cerinta2.2.csv", index=False)