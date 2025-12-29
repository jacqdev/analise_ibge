import pandas as pd

def calcular_media_renda(dados: pd.DataFrame) -> float:
    """
    Calcula a média da coluna 'renda_media' de um DataFrame.
    """
    # Padroniza os nomes das colunas para minúsculo e sem espaços
    dados.columns = dados.columns.str.strip().str.lower()
    if "renda_media" in dados.columns:
        return dados["renda_media"].mean()
    else:
        raise KeyError("Coluna 'renda_media' não encontrada no DataFrame.")

def calcular_taxa_desemprego_media(dados: pd.DataFrame) -> float:
    """
    Calcula a média da coluna 'desemprego' de um DataFrame.
    """
    dados.columns = dados.columns.str.strip().str.lower()
    if "desemprego" in dados.columns:
        return dados["desemprego"].mean()
    else:
        raise KeyError("Coluna 'desemprego' não encontrada no DataFrame.")
