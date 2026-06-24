from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    print("Iniciando pipeline...")

    df = extract_data()
    print("Dados extraídos:", len(df), "linhas")

    df_tratado = transform_data(df)
    print("Dados tratados:", len(df_tratado), "linhas")

    load_data(df_tratado)

    print("Pipeline finalizado com sucesso!")

if __name__ == "__main__":
    main()