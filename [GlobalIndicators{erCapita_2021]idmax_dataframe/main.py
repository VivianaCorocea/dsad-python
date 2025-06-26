import pandas as pd

indicatori_df = pd.read_csv("GlobalIndicatorsPerCapita_2021.csv")

ramuri = ["AgrHuntForFish","Construction","Manufacturing","MiningManUt","TradeT","TransportComm","Other"]

indicatori_copie_df = indicatori_df.copy()

indicatori_copie_df = indicatori_copie_df[ramuri].idxmax(axis=1)

rezultat1 = pd.DataFrame(
    {
        "CountryID":indicatori_df["CountryID"],
        "Country":indicatori_df["Country"],
        "Ramura Dominanta": indicatori_copie_df
    }
)

rezultat1.to_csv("Cerinta1.csv", index=False)

#cerinta2
coduri_df = pd.read_csv("CoduriTari.csv")

merged_df = pd.merge(
    coduri_df[["CountryID","Continent"]],
    indicatori_df, on="CountryID", how="inner"
)

variabile_numerice = ["GNI","ChangesInv","Exports","Imports","FinalConsExp","GrossCF","HouseholdConsExp","AgrHuntForFish","Construction","Manufacturing","MiningManUt","TradeT","TransportComm","Other"]

merged_df = merged_df.groupby(by="Continent")[variabile_numerice].mean().round(2)

merged_df.reset_index(inplace=True)

merged_df.to_csv("Cerinta1.csv", index=False)