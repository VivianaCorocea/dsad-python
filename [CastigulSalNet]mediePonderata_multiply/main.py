import pandas as pd

#cerinta1
castig_df = pd.read_csv("CastigulSalNet.csv")

castig_copie_df = castig_df.copy()

perioada = ["2016","2017","2018","2019","2020","2021"]

castig_copie_df["Media"] = castig_copie_df[perioada].mean(axis=1)

rezultat1 = pd.DataFrame(
    {
        "Indicativ":castig_copie_df["Indicativ"],
        "Judet":castig_copie_df["Judet"],
        "Media":castig_copie_df["Media"]
    }
)

rezultat1.sort_values("Media", ascending=False, inplace=True)

rezultat1.to_csv("Cerinta1.csv", index=False)

#cerinta2
populatie_df = pd.read_csv("PopulatieJudete.csv")

populatie_copie_df = populatie_df.copy()

merged_df = pd.merge(
    populatie_copie_df[["Indicativ","Regiune","Populatie"]],
    castig_copie_df[["Indicativ","2016","2017","2018","2019","2020","2021"]], on="Indicativ", how="inner"
)


suma_populatie = merged_df.groupby(by="Regiune")["Populatie"].sum()

salarii_ponderate = merged_df[perioada].multiply(merged_df["Populatie"], axis=0)
salarii_ponderate["Regiune"] = merged_df["Regiune"]

grupare = salarii_ponderate.groupby(by="Regiune")[perioada].sum()

rezultat2 = grupare.div(suma_populatie, axis=0).round(2)

rezultat2.reset_index(inplace=True)

rezultat2.to_csv("Cerinta2.csv", index=False)