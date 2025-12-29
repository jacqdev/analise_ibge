import pandas as pd
import src.limpeza as limpeza

def test_remover_nulos():
    dados = pd.DataFrame({"ano":[2020, None], "renda_media":[2000, None]})
    df = limpeza.remover_nulos(dados)
    assert df.shape[0] == 1
    assert df.iloc[0]["ano"] == 2020

def test_remover_duplicados():
    dados = pd.DataFrame({"ano":[2020,2020], "renda_media":[2000,2000]})
    df = limpeza.remover_duplicados(dados)
    assert df.shape[0] == 1
