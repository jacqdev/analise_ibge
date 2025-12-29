import pandas as pd

def remover_nulos(dados: pd.DataFrame) -> pd.DataFrame:
    """
    Remove linhas com valores nulos.
    """
    return dados.dropna()

def remover_duplicados(dados: pd.DataFrame) -> pd.DataFrame:
    """
    Remove linhas duplicadas.
    """
    return dados.drop_duplicates()
