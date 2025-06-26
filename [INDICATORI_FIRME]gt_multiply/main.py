import pandas as pd

#cerinta1
indicatori_df = pd.read_csv("Indicatori.csv")

indicatori_copy_df = indicatori_df.copy()

medie_cfa_tara = indicatori_copy_df["CFA"].mean()

cfa_mai_mare_decat_medie = indicatori_copy_df["CFA"].gt(medie_cfa_tara)

indicatori_copy_df = indicatori_copy_df[cfa_mai_mare_decat_medie]

indicatori_copy_df.sort_values("CFA", ascending=False, inplace=True)

indicatori_copy_df.to_csv("Cerinta1.csv", index=False)

#cerinta2
populatie = pd.read_csv("PopulatieLocalitati.csv")

populatie_copy = populatie.copy()
indicatori_copy = indicatori_df.copy()

valori = ["NR_FIRME","NSAL","CFA","PROFITN","PIERDEREN"]

populatie_copy.rename(columns={"Siruta":"SIRUTA"}, inplace=True)

merged_df = pd.merge(
    populatie_copy[["SIRUTA","Judet","Populatie"]],
    indicatori_copy, on="SIRUTA", how="inner"
)

grupare_valori = merged_df.groupby(by="Judet")[valori].sum()

grupare_populatie = merged_df.groupby(by="Judet")["Populatie"].sum()

rezultat2 = grupare_valori[valori].multiply(1000, axis=0)

rezultat2 = rezultat2.div(grupare_populatie, axis=0).round(3)

rezultat2.reset_index(inplace=True)

rezultat2.to_csv("Cerinta2.csv", index=False)
