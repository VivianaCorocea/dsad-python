import pandas as pd

#cerinta1
diversitate_df = pd.read_csv("Diversitate.csv")

diversitate_copy_df = diversitate_df.copy()

ani = ["2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"]

medie_ani = diversitate_copy_df[ani].mean(axis=1)

rezultat1 = pd.DataFrame(
    {
        "Siruta":diversitate_copy_df["Siruta"],
        "Localitate":diversitate_copy_df["Localitate"],
        "Diversitate":medie_ani
    }
)

rezultat1.sort_values("Diversitate", ascending=False, inplace=True)

rezultat1.to_csv("Cerinta1.csv", index=False)

#cerinta2
coduri = pd.read_csv("Coduri_Localitati.csv")

coduri_copy = coduri.copy()
diversitate_copy = diversitate_df.copy()

diversitate_copy.drop(columns=["Localitate"], inplace=True)

merg_df = pd.merge(
    coduri_copy[["Siruta", "Judet"]],
    diversitate_copy, on="Siruta", how="inner"
)

masca = merg_df[ani].eq(0)

masca["Judet"] = merg_df["Judet"]

grupare = masca.groupby(by="Judet")[ani].sum()

grupare.reset_index(inplace=True)

grupare.to_csv("Cerinta2.csv", index=False)