import pandas as pd

def load_database_info(csv_path):
    """
    Carrega as informações do banco de dados a partir de um arquivo CSV.

    Args:
        csv_path (str): Caminho para o arquivo CSV contendo as informações do banco de dados.

    Returns:
        pd.DataFrame: DataFrame com as informações do banco de dados.
    """
    return pd.read_csv(csv_path)
