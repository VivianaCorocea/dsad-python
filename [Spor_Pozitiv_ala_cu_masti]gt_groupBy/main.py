import pandas as pd

#cerintra1
miscare_df = pd.read_csv("MiscareaNaturala.csv")

miscare_copy_df = miscare_df.copy()

mai_mare_decat_zero = miscare_copy_df["RS"].gt(0)

miscare_copy_df = miscare_copy_df[mai_mare_decat_zero]

miscare_copy_df.sort_values("RS", ascending=False)

miscare_copy_df[["Country_Number","Country_Name","RS"]].to_csv("Cerinta1.csv", index=False)

#cerinta2
coduri = pd.read_csv("CoduriTariExtins.csv")
miscare = pd.read_csv("MiscareaNaturala.csv")

coduri_copy = coduri.copy()
miscare_copy = miscare_df.copy()

indicatori = ["FR","IM","LE","LEF","LEM","MMR","RS"]

merged_df = pd.merge(
    coduri_copy[["Country_Number", "Continent_Name"]],
    miscare_copy[["Country_Number","FR","IM","LE","LEF","LEM","MMR","RS"]], on="Country_Number", how="inner"
)

grupare = merged_df.groupby(by="Continent_Name")[indicatori].mean()

rs_mediu_mondial = merged_df["RS"].mean()

mai_mare_decat_medie = grupare["RS"].gt(rs_mediu_mondial)

rezultat2 = grupare[mai_mare_decat_medie]
rezultat2.reset_index(inplace=True)
rezultat2.to_csv("Cerinta2.csv", index=False)