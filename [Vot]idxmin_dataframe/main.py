import pandas as pd

#cerinta1
vot_df = pd.read_csv("Vot.csv")

vot_copy_df = vot_df.copy()

votanti = ["Barbati_25-34","Barbati_35-44","Barbati_45-64","Barbati_65_","Femei_18-24","Femei_35-44","Femei_45-64","Femei_65_"]

vot_copy_df["Categorie"] = vot_copy_df[votanti].idxmin(axis=1)

rezultat1 = pd.DataFrame(
    {
        "Siruta":vot_copy_df["Siruta"],
        "Localitate":vot_copy_df["Localitate"],
        "Categorie":vot_copy_df["Categorie"]
    }
)

rezultat1.to_csv("Cerinta1.csv", index=False)

#cerinta2
coduri_df = pd.read_csv("Coduri_localitati.csv")

coduri_copy_df = coduri_df.copy()
vot_copie = vot_df.copy()

merged_df = pd.merge(
    coduri_copy_df,
    vot_copie[["Siruta","Barbati_25-34","Barbati_35-44","Barbati_45-64","Barbati_65_","Femei_18-24","Femei_35-44","Femei_45-64","Femei_65_"]], on="Siruta", how="inner"
)

merged_df = merged_df.groupby(by="Judet")[votanti].mean()
merged_df.reset_index(inplace=True)

merged_df.rename(columns={"Judet":"County"}, inplace=True)

merged_df.to_csv("Cerinta2.csv", index=False)