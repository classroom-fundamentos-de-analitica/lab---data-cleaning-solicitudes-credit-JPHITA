"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df.drop(columns="Unnamed: 0", inplace=True)

    df.dropna(inplace=True)

    df["sexo"] = df["sexo"].str.lower()

    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()

    df["idea_negocio"] = df["idea_negocio"].str.lower()
    df["idea_negocio"] = df["idea_negocio"].str.replace(r"[\-_]", " ", regex=True)

    df["barrio"] = df["barrio"].str.lower()
    df["barrio"] = df["barrio"].str.replace(r"[\-_]", " ", regex=True)

    pd.to_datetime(df["fecha_de_beneficio"])
    df.loc[df["fecha_de_beneficio"].str.match(r"\d{4}\/\d{2}\/\d{1,2}") , "fecha_de_beneficio"] = pd.to_datetime(
        df.loc[df["fecha_de_beneficio"].str.match(r"\d{4}\/\d{2}\/\d{1,2}") , "fecha_de_beneficio"],
        format="%Y/%m/%d"
    )

    df.loc[~df["fecha_de_beneficio"].str.match(r"\d{4}\/\d{2}\/\d{1,2}").fillna(True) , "fecha_de_beneficio"] = pd.to_datetime(
        df.loc[~df["fecha_de_beneficio"].str.match(r"\d{4}\/\d{2}\/\d{1,2}").fillna(True) , "fecha_de_beneficio"],
        format="%d/%m/%Y"
    )

    df["monto_del_credito"] = df["monto_del_credito"].str.replace(r"[$,]", "", regex=True)
    df["monto_del_credito"] = pd.to_numeric(df["monto_del_credito"])

    df["línea_credito"] = df["línea_credito"].str.lower()
    df["línea_credito"] = df["línea_credito"].str.replace(r"[\-_]", " ", regex=True)

    df.drop_duplicates(inplace=True)
    

    return df
