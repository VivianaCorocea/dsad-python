import pandas as pd

#cerinta1
populatie_df = pd.read_csv("MiseNatPopTari.csv")

populatie_copie_df = populatie_df.copy()

indicatori_numerici = ["RS","FR","LM","MMR","LE","LEM","LEF"]

spor_negativ = populatie_copie_df["RS"].lt(0)

populatie_copie_df = populatie_df[spor_negativ]

populatie_copie_df.to_csv("Cerinta1.csv", index=False)

#cerinta2
coduri_df = pd.read_csv("CoduriTariExtins.csv")

merged_df = pd.merge(
    coduri_df[["Country_Name", "Continent"]],
    populatie_df[["Country_Name","RS","FR","LM","MMR","LE","LEM","LEF"]], on="Country_Name", how="inner"
)

merged_df = merged_df.groupby(by="Continent")[indicatori_numerici].mean()

merged_df.reset_index(inplace=True)

merged_df = merged_df.sort_values("FR", ascending=True)

merged_df.to_csv("Cerinta2.csv", index=False)