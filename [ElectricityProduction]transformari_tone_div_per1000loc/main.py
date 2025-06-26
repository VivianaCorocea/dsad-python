import pandas as pd

#cerinta1
emisii_df = pd.read_csv("Emissions.csv")

emisii_copy_df = emisii_df.copy()

variabile = ["AirEmiss","Sulphur","Nitrogen","Ammonia","NonMeth","Partic","GreenGE","GreenGIE"]

variabile_mii_tone = ["GreenGE","GreenGIE"]

emisii_copy_df["GreenGE"] = emisii_copy_df["GreenGE"]*1000
emisii_copy_df["GreenGIE"] = emisii_copy_df["GreenGIE"]*1000

emisii_copy_df = emisii_copy_df[variabile].sum(axis=1)

rezultat1 = pd.DataFrame(
    {
        "CountryCode":emisii_df["CountryCode"],
        "Country":emisii_df["Country"],
        "Emisii_total_tone":emisii_copy_df
    }
)

rezultat1.to_csv("Cerinta1.csv", index=False)

#cerinta2
populatie_df = pd.read_csv("PopulatieEuropa.csv")

emisii_copie_df = emisii_df.copy()
populatie_copy_df = populatie_df.copy()
populatie_copy_df.rename(columns={"Code":"CountryCode"}, inplace=True)

merged_df = pd.merge(
    populatie_copy_df[["CountryCode","Region","Population"]],
    emisii_copie_df[["CountryCode","AirEmiss","Sulphur","Nitrogen","Ammonia","NonMeth","Partic","GreenGE","GreenGIE"]], on="CountryCode", how="inner"
)

merged_df["GreenGE"] = merged_df["GreenGE"]*1000
merged_df["GreenGIE"] = merged_df["GreenGIE"]*1000

suma_emisii = merged_df.groupby(by="Region")[variabile].sum()
print(suma_emisii)
suma_populatie = merged_df.groupby(by="Region")["Population"].sum()
print(suma_populatie)

rezultat2 = suma_emisii.div(suma_populatie, axis=0)*100000
rezultat2 = rezultat2.round(2)

rezultat2.reset_index(inplace=True)

rezultat2.to_csv("Cerinta2.csv", index=False)