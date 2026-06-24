def load_data(df):
    df.to_csv(
        "data/processed/acidentes_prf_2024_2025_tratado.csv",
        sep=";",
        index=False,
        encoding="utf-8-sig"
    )

    print("Arquivo tratado salvo em data/processed/")