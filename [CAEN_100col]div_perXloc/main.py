import pandas as pd

#cerinta1
caen_df = pd.read_csv("CAEN2_2021_NSAL.csv")

caen_copy_df = caen_df.copy()

ramuri = caen_copy_df.columns.drop("SIRUTA")

caen_copy_df["Suma"] = caen_copy_df[ramuri].sum(axis=1)

procente = caen_copy_df[ramuri].div(caen_copy_df["Suma"], axis=0)

procente = procente*100

procente["SIRUTA"] = caen_df["SIRUTA"]

rezultat = pd.DataFrame(
    {
        "SIRUTA":caen_df["SIRUTA"],
    }
)

rezultat[ramuri] = procente[ramuri]

rezultat.to_csv("Cerinta1.csv", index=False)

#cerinta2
populatie = pd.read_csv("PopulatieLocalitati.csv")

populatie_copy = populatie.copy()
caen_copy = caen_df.copy()

populatie_copy.rename(columns={"Siruta":"SIRUTA"}, inplace=True)

merge_df = pd.merge(
    populatie_copy[["SIRUTA","Judet","Populatie"]],
    caen_copy, on="SIRUTA", how="inner"
)

grupare = merge_df.groupby(by="Judet")[ramuri].sum()

pop = merge_df.groupby(by="Judet")["Populatie"].sum()

rezultat = (grupare*100000).div(pop, axis=0)

rezultat = rezultat.round(2)

rezultat.reset_index(inplace=True)

rezultat.to_csv("Cerinta2.csv", index=False)