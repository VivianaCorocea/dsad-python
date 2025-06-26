import pandas as pd

#cerinta1
indicatori_df = pd.read_csv("GlobalIndicatorsPerCapita_2021_Extended.csv")

linia_noua_din_tabel = ["AgriHuntForFish","Construction","Manufacturing","MiningManU","TradeT","TransportComm","Other"]

indicatori_copie_df = indicatori_df.copy()

indicatori_copie_df["Valoare Adaugata"] = indicatori_copie_df[linia_noua_din_tabel].sum(axis=1)

rezultat1 = pd.DataFrame(
    {
        "CountryID":indicatori_copie_df["Cod"],
        "Country":indicatori_copie_df["Tara"],
        "Valoare Adaugata":indicatori_copie_df["Valoare Adaugata"]
    }
)

rezultat1.to_csv("Cerinta1.csv", index=False)

#cerinta2
tari_df = pd.read_csv("CountryCodes_Extended.csv")

valori = ["GNI","Changesinv","Exports","Imports","FinalConsExp","GrossCF","HouseholdConsExp"]+linia_noua_din_tabel
indicatori_copie2_df = indicatori_df.copy()
indicatori_copie2_df = indicatori_copie2_df.drop(columns=["Tara"])

merged_df = pd.merge(
    tari_df[["Cod","Continent"]],
    indicatori_copie2_df, on="Cod", how="inner"
)

merged_df = merged_df.groupby(by="Continent")[valori]

medii_continente = merged_df.mean()
abateri_continent = merged_df.std()

variatii_standard = (abateri_continent/medii_continente) * 100
variatii_standard.reset_index(inplace=True)

variatii_standard.to_csv("Cerinta2.csv", index=False)