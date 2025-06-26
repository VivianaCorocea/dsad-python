import pandas as pd

#cerinta1
netflix_df = pd.read_csv("Netflix.csv")

netflix_copy_df = netflix_df.copy()

valori = ["Librarie","CostLunarBasic","CostLunarStandard","CostLunarPremium","Internet","HDI","Venit","IndiceFericire","IndiceEducatie"]

medie = netflix_copy_df[valori].mean()
std = netflix_copy_df[valori].std(ddof=0)

netflix_copy_df[valori] = ((netflix_copy_df[valori]-medie)/std).round(3)

netflix_copy_df.sort_values("Internet", ascending=False, inplace=True)

netflix_copy_df[["Cod","Tara"]+valori].to_csv("Cerinta1.csv", index=False)

#cerinta2
coduri = pd.read_csv("CoduriTari.csv")

coduri_copy = coduri.copy()
netflix_copy = netflix_df.copy()

merge_df = pd.merge(
    coduri_copy[["Cod","Continent"]],
    netflix_copy[["Cod"]+valori], on="Cod", how="inner"
)

abatere_standard_continent = merge_df.groupby(by="Continent")[valori].std(ddof=0)
medie_continente = merge_df.groupby(by="Continent")[valori].mean()

rezultat2 = (abatere_standard_continent/medie_continente).round(3)

rezultat2.sort_values("Librarie", ascending=False, inplace=True)

rezultat2.reset_index(inplace=True)

rezultat2.to_csv("Cerinta2.csv", index=False)