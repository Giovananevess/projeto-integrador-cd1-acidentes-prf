import pandas as pd

def transform_data(df):
    # Padronizar nomes das colunas
    df.columns = df.columns.str.lower().str.strip()

    # Converter data
    df["data_inversa"] = pd.to_datetime(
        df["data_inversa"],
        format="%d/%m/%Y",
        errors="coerce"
    )

    # Criar coluna ano
    df["ano"] = df["data_inversa"].dt.year

    # Criar coluna mês
    df["mes"] = df["data_inversa"].dt.month

    # Garantir campos numéricos
    colunas_numericas = [
        "pessoas",
        "mortos",
        "feridos_leves",
        "feridos_graves",
        "ilesos",
        "ignorados",
        "feridos",
        "veiculos"
    ]

    for coluna in colunas_numericas:
        df[coluna] = pd.to_numeric(df[coluna], errors="coerce").fillna(0).astype(int)

    # Tratar latitude e longitude
    df["latitude"] = df["latitude"].astype(str).str.replace(",", ".", regex=False)
    df["longitude"] = df["longitude"].astype(str).str.replace(",", ".", regex=False)

    df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
    df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

    # Remover linhas sem id
    df = df.dropna(subset=["id"])

    return df