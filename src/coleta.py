import pandas as pd

def carregar_csv(caminho: str) -> pd.DataFrame:
    """
    Carrega um arquivo CSV, padroniza os nomes das colunas e retorna um DataFrame.
    
    Parâmetros:
        caminho (str): Caminho do arquivo CSV.
    
    Retorna:
        pd.DataFrame: DataFrame com colunas padronizadas.
    
    Levanta:
        FileNotFoundError: Se o arquivo não for encontrado.
        RuntimeError: Se ocorrer outro erro ao carregar o CSV.
    """
    try:
        df = pd.read_csv(caminho, sep=",", encoding="utf-8")
        # Remove espaços e coloca tudo em minúsculo para evitar erros
        df.columns = df.columns.str.strip().str.lower()
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    except Exception as e:
        raise RuntimeError(f"Erro ao carregar CSV: {e}")
