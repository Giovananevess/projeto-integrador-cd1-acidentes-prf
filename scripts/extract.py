import pandas as pd

def extract_data():
    df_2024 = pd.read_csv("data/raw/acidentes_prf_2024.csv", sep=";", encoding="latin1")
    df_2025 = pd.read_csv("data/raw/acidentes_prf_2025.csv", sep=";", encoding="latin1")

    df = pd.concat([df_2024, df_2025], ignore_index=True)

    return df