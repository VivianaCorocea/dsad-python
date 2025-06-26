import pandas as pd

#cerinta1
alcol_df = pd.read_csv("alcohol.csv")

ani = ["2000","2005","2010","2015","2018"]

alcol_medie = alcol_df.copy()
alcol_medie["Media"] = alcol_df[ani].mean(axis=1)

rezultat1 = pd.DataFrame(
    {
        "Code":alcol_df["Code"],
        "Media":alcol_medie["Media"]
    }
)

rezultat1.to_csv("Cerinta1.csv", index=False)

#cerinta2
coduri_df = pd.read_csv("CoduriTariExtins.csv")

alcol_df.rename(columns={"Entity":"Tari"}, inplace=True)

alcol_fara_code = alcol_df.drop(columns=["Code"])

merged_df = pd.merge(
    coduri_df[["Continent", "Tari"]],
    alcol_fara_code, on="Tari", how="inner"
)

merged_df = merged_df.groupby(by="Continent")[ani]

merged_medie = merged_df.mean()
merged_medie.reset_index(inplace=True)
print(merged_medie)

anul = merged_medie[ani].idxmax(axis=1)

rezultat2 = pd.DataFrame(
    {
        "Continent_Name":merged_medie["Continent"],
        "Anul":anul
    }
)

rezultat2.to_csv("Cerinta2.csv", index=False)
